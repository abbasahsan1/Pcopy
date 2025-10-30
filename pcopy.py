#!/usr/bin/env python3
"""
pcopy - A cross-platform CLI tool to merge text files and copy to clipboard
Version: 1.0.0
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Set
import re

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False
    print("⚠️  Warning: pyperclip not installed. Clipboard functionality disabled.")
    print("   Install with: pip install pyperclip")

try:
    import pathspec
    PATHSPEC_AVAILABLE = True
except ImportError:
    PATHSPEC_AVAILABLE = False
    print("⚠️  Warning: pathspec not installed. .pcopyignore support limited.")
    print("   Install with: pip install pathspec")


# Default ignore patterns (applied even without .pcopyignore)
DEFAULT_IGNORE_PATTERNS = [
    '.git/',
    '.git/**',
    '.idea/',
    '.idea/**',
    '__pycache__/',
    '__pycache__/**',
    'node_modules/',
    'node_modules/**',
    '.vscode/',
    '.vscode/**',
    '.vs/',
    '.vs/**',
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '.DS_Store',
    'Thumbs.db',
]

# Text file extensions whitelist
TEXT_EXTENSIONS = {
    '.txt', '.md', '.csv', '.json', '.yaml', '.yml', '.xml', '.html', '.css', '.scss',
    '.py', '.js', '.ts', '.tsx', '.jsx', '.c', '.cpp', '.h', '.hpp', '.cs', '.java',
    '.php', '.rb', '.go', '.rs', '.ini', '.cfg', '.conf', '.sh', '.bat', '.sql',
    '.toml', '.lock', '.gitignore', '.env', '.properties', '.gradle', '.maven',
    '.r', '.R', '.swift', '.kt', '.scala', '.pl', '.lua', '.vim', '.tex',
    '.rst', '.adoc', '.dockerfile', '.makefile', '.cmake', '.proto', '.graphql',
}

# Binary file extensions blacklist
BINARY_EXTENSIONS = {
    '.exe', '.dll', '.so', '.dylib', '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg', '.webp', '.tiff',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.obj', '.apk',
    '.bin', '.iso', '.dmg', '.pkg', '.deb', '.rpm', '.mp4', '.mp3', '.wav',
    '.avi', '.mov', '.wmv', '.flac', '.ogg', '.woff', '.woff2', '.ttf', '.eot',
    '.db', '.sqlite', '.sqlite3', '.class', '.jar', '.war', '.ear', '.pyc',
    '.pyo', '.pyd', '.o', '.a', '.lib', '.exp', '.ilk', '.pdb', '.tmp', '.cache',
    '.log', '.lock', '.meta', '.asset', '.prefab', '.unity', '.blend', '.fbx',
}

# Maximum file size (5 MB)
MAX_FILE_SIZE = 5 * 1024 * 1024


class FileFilter:
    """Handles file filtering based on patterns and file types"""
    
    def __init__(self, root_path: Path):
        self.root_path = root_path
        self.spec = None
        self.load_ignore_patterns()
    
    def load_ignore_patterns(self):
        """Load .pcopyignore file if it exists"""
        ignore_file = self.root_path / '.pcopyignore'
        patterns = DEFAULT_IGNORE_PATTERNS.copy()
        
        if ignore_file.exists():
            try:
                with open(ignore_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            patterns.append(line)
            except Exception as e:
                print(f"⚠️  Warning: Could not read .pcopyignore: {e}")
        
        if PATHSPEC_AVAILABLE:
            self.spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)
        else:
            # Fallback: simple pattern matching
            self.patterns = patterns
    
    def should_ignore(self, file_path: Path) -> bool:
        """Check if file should be ignored based on patterns"""
        try:
            relative_path = file_path.relative_to(self.root_path)
            path_str = str(relative_path).replace('\\', '/')
            
            # Check if it's a hidden file (starts with .)
            if any(part.startswith('.') for part in relative_path.parts):
                # Allow .pcopyignore and other explicitly allowed files
                if relative_path.name != '.pcopyignore':
                    return True
            
            if PATHSPEC_AVAILABLE and self.spec:
                return self.spec.match_file(path_str)
            else:
                # Fallback pattern matching
                return self._simple_match(path_str)
        except ValueError:
            return True
    
    def _simple_match(self, path_str: str) -> bool:
        """Simple pattern matching fallback"""
        for pattern in self.patterns:
            pattern = pattern.strip()
            if not pattern or pattern.startswith('#'):
                continue
            
            # Handle negation
            if pattern.startswith('!'):
                continue  # Skip negation in simple mode
            
            # Simple wildcard matching
            if '**' in pattern:
                pattern = pattern.replace('**', '.*')
            pattern = pattern.replace('*', '[^/]*')
            pattern = pattern.replace('?', '.')
            
            if re.search(pattern, path_str):
                return True
        
        return False


def is_text_file(file_path: Path) -> bool:
    """Determine if a file is text-based"""
    # Check extension first
    ext = file_path.suffix.lower()
    
    if ext in BINARY_EXTENSIONS:
        return False
    
    if ext in TEXT_EXTENSIONS or ext == '':
        return True
    
    # Binary content detection
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(4096)
            if not chunk:
                return True  # Empty file
            
            # Check for null bytes (strong indicator of binary)
            if b'\x00' in chunk:
                return False
            
            # Check ratio of non-printable characters
            non_printable = sum(1 for byte in chunk if byte < 32 and byte not in (9, 10, 13))
            if non_printable / len(chunk) > 0.3:
                return False
            
        return True
    except Exception:
        return False


def read_file_content(file_path: Path) -> str:
    """Read file content with encoding fallback"""
    # Try to detect encoding from BOM first
    try:
        with open(file_path, 'rb') as f:
            raw = f.read()
            
        # Check for BOM markers
        if raw.startswith(b'\xff\xfe\x00\x00'):
            encoding = 'utf-32-le'
        elif raw.startswith(b'\x00\x00\xfe\xff'):
            encoding = 'utf-32-be'
        elif raw.startswith(b'\xff\xfe'):
            encoding = 'utf-16-le'
        elif raw.startswith(b'\xfe\xff'):
            encoding = 'utf-16-be'
        elif raw.startswith(b'\xef\xbb\xbf'):
            encoding = 'utf-8-sig'
        else:
            encoding = None
        
        # If BOM detected, decode with that encoding
        if encoding:
            try:
                return raw.decode(encoding)
            except UnicodeDecodeError:
                pass
    except Exception:
        pass
    
    # Fallback to trying multiple encodings
    encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 
                 'latin-1', 'cp1252', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception as e:
            print(f"⚠️  Warning: Could not read {file_path}: {e}")
            return ""
    
    return ""


def generate_file_tree(root_path: Path, file_filter: FileFilter, text_files: Set[Path]) -> str:
    """Generate ASCII file tree structure"""
    tree_lines = [f"{root_path.name}/"]
    
    def add_directory(dir_path: Path, prefix: str = ""):
        try:
            entries = sorted(dir_path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        except PermissionError:
            return
        
        dirs = [e for e in entries if e.is_dir() and not file_filter.should_ignore(e)]
        files = [e for e in entries if e.is_file() and e in text_files]
        
        all_items = dirs + files
        
        for i, item in enumerate(all_items):
            is_last = i == len(all_items) - 1
            connector = "└── " if is_last else "├── "
            
            if item.is_dir():
                tree_lines.append(f"{prefix}{connector}{item.name}/")
                extension = "    " if is_last else "│   "
                add_directory(item, prefix + extension)
            else:
                tree_lines.append(f"{prefix}{connector}{item.name}")
    
    add_directory(root_path)
    return "\n".join(tree_lines)


def collect_text_files(root_path: Path, file_filter: FileFilter) -> Tuple[List[Path], int]:
    """Collect all text files in directory"""
    text_files = []
    ignored_count = 0
    
    for file_path in root_path.rglob('*'):
        if not file_path.is_file():
            continue
        
        # Skip PROMPT.txt itself
        if file_path.name == 'PROMPT.txt':
            continue
        
        # Check file size
        try:
            if file_path.stat().st_size > MAX_FILE_SIZE:
                ignored_count += 1
                continue
        except Exception:
            ignored_count += 1
            continue
        
        # Check if ignored
        if file_filter.should_ignore(file_path):
            ignored_count += 1
            continue
        
        # Check if text file
        if is_text_file(file_path):
            text_files.append(file_path)
    
    return sorted(text_files), ignored_count


def create_prompt_file(root_path: Path, text_files: List[Path], 
                       include_tree: bool, file_filter: FileFilter) -> str:
    """Create the merged PROMPT.txt content"""
    content_parts = []
    
    # Add file tree if requested
    if include_tree:
        content_parts.append("=" * 66)
        content_parts.append("📁 FILE TREE")
        content_parts.append("=" * 66)
        content_parts.append("")
        
        tree = generate_file_tree(root_path, file_filter, set(text_files))
        content_parts.append(tree)
        content_parts.append("")
    
    # Add file contents
    content_parts.append("=" * 66)
    content_parts.append("📄 FILE CONTENTS")
    content_parts.append("=" * 66)
    content_parts.append("")
    
    for file_path in text_files:
        try:
            relative_path = file_path.relative_to(root_path)
            content = read_file_content(file_path)
            
            content_parts.append(f"Filename: {relative_path}")
            content_parts.append("Content:")
            content_parts.append("{")
            content_parts.append(content)
            content_parts.append("}")
            content_parts.append("")
            content_parts.append("-" * 66)
            content_parts.append("")
        except Exception as e:
            print(f"⚠️  Warning: Could not process {file_path}: {e}")
    
    return "\n".join(content_parts)


def copy_to_clipboard(content: str) -> bool:
    """Copy content to system clipboard"""
    if not CLIPBOARD_AVAILABLE:
        print("⚠️  Warning: Clipboard copy skipped (pyperclip not installed)")
        return False
    
    try:
        pyperclip.copy(content)
        return True
    except Exception as e:
        print(f"⚠️  Warning: Could not copy to clipboard: {e}")
        return False


def format_size(size_bytes: int) -> str:
    """Format byte size to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.0f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.0f} TB"


def main():
    parser = argparse.ArgumentParser(
        description='pcopy - Merge text files and copy to clipboard',
        usage='pcopy [tree] [path]'
    )
    parser.add_argument('args', nargs='*', help='Optional: tree and/or path')
    
    args = parser.parse_args()
    
    # Parse arguments
    include_tree = False
    target_path = Path.cwd()
    
    for arg in args.args:
        if arg.lower() == 'tree':
            include_tree = True
        else:
            target_path = Path(arg)
    
    # Validate path
    if not target_path.exists():
        print(f"❌ Error: Directory not found: {target_path}")
        sys.exit(1)
    
    if not target_path.is_dir():
        print(f"❌ Error: Not a directory: {target_path}")
        sys.exit(1)
    
    # Print header
    print("\n🧩 pcopy v1.0.0")
    print(f"📂 Target directory: {target_path.absolute()}")
    
    # Initialize file filter
    file_filter = FileFilter(target_path)
    
    # Collect text files
    text_files, ignored_count = collect_text_files(target_path, file_filter)
    
    if not text_files:
        print("⚠️  No text files found in directory.")
        sys.exit(0)
    
    print(f"📄 {len(text_files)} text files detected ({ignored_count} ignored)")
    
    if include_tree:
        print("🌳 File tree included")
    
    # Create merged content
    print("✍️  Writing PROMPT.txt...")
    content = create_prompt_file(target_path, text_files, include_tree, file_filter)
    
    # Write to file
    output_file = target_path / 'PROMPT.txt'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"❌ Error: Could not write PROMPT.txt: {e}")
        sys.exit(1)
    
    # Copy to clipboard
    content_size = len(content.encode('utf-8'))
    if copy_to_clipboard(content):
        print(f"📋 Copied content to clipboard ({format_size(content_size)})")
    
    print(f"✅ Done! File saved at {output_file.absolute()}")
    print()


if __name__ == '__main__':
    main()

# pcopy - Project Copy Tool

[![GitHub release](https://img.shields.io/github/v/release/abbasahsan1/Pcopy)](https://github.com/abbasahsan1/Pcopy/releases/latest)
[![License](https://img.shields.io/github/license/abbasahsan1/Pcopy)](LICENSE)

A cross-platform command-line tool that reads all text-based files in a specified folder, merges them into a single file called `PROMPT.txt`, and copies its entire content to the clipboard.

**Perfect for preparing code context for AI assistants like ChatGPT and Claude!**

## 📥 Quick Install

### Option 1: Standalone Executable (Windows - Recommended)
**No Python required!**

1. Download the latest release: [pcopy-windows-x64.zip](https://github.com/abbasahsan1/Pcopy/releases/latest)
2. Extract and run: `pcopy.exe tree`
3. Done! ✅

### Option 2: Python Script (All Platforms)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Add to PATH for global access:

### Windows
```powershell
# Add the script directory to PATH (replace with your actual path)
$env:Path += ";X:\Pcopy"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User)
```

### Linux/WSL/Mac
```bash
# Create a symbolic link
sudo ln -s /path/to/pcopy/pcopy.py /usr/local/bin/pcopy
chmod +x /path/to/pcopy/pcopy.py

# Or add to .bashrc/.zshrc
echo 'alias pcopy="python3 /path/to/pcopy/pcopy.py"' >> ~/.bashrc
```

## Usage

```bash
pcopy [tree] [path]
```

### Arguments
- `path` - (Optional) Path to the target directory. If omitted, uses the current working directory.
- `tree` - (Optional keyword) If included, generates and prepends a file tree structure in the output.

### Examples

```bash
# Use current directory, no file tree
pcopy

# Use specific directory
pcopy /home/user/project

# Add file tree for current directory
pcopy tree

# Add file tree for given path
pcopy tree "C:\Projects\App"

# On Windows with Python
python pcopy.py tree .
```

## Features

### 📁 File Tree Generation
When the `tree` argument is used, pcopy generates an ASCII tree structure showing the hierarchy of all included files.

### 📄 Text File Detection
Automatically identifies text files based on:
- Extension whitelist (`.py`, `.js`, `.md`, `.json`, etc.)
- Binary content detection
- File size limits (5 MB max)

### 🚫 .pcopyignore Support
Create a `.pcopyignore` file in your project root using `.gitignore` syntax:

```
# Ignore build artifacts
build/
dist/
*.log

# Ignore secrets
.env
secrets.json

# Keep configs even if in ignored dirs
!config.yaml
```

### 📋 Clipboard Integration
Automatically copies the merged content to your system clipboard (requires `pyperclip`).

### 🔍 Smart Filtering
Automatically ignores:
- Binary files (`.exe`, `.dll`, `.zip`, `.jpg`, etc.)
- Hidden files and folders
- Common directories (`.git`, `node_modules`, `__pycache__`, etc.)
- Files larger than 5 MB

## Output Format

The generated `PROMPT.txt` includes:

```
==================================================================
📁 FILE TREE
==================================================================

project/
├── main.py
├── config.yaml
└── utils/
    ├── helper.py
    └── logger.py

==================================================================
📄 FILE CONTENTS
==================================================================

Filename: main.py
Content:
{
print("Hello world!")
}

------------------------------------------------------------------
```

## Dependencies

- `pyperclip` - Cross-platform clipboard support
- `pathspec` - .gitignore-style pattern matching

## Use Cases

### 1. Prepare Context for AI Assistants
```bash
cd my-project
pcopy tree
# Paste clipboard into ChatGPT/Claude with your question!
```

### 2. Code Reviews
```bash
pcopy tree feature-branch/
# Share PROMPT.txt with reviewers
```

### 3. Project Documentation
```bash
pcopy tree
# Quick overview of entire codebase
```

### 4. Project Snapshots
```bash
# Generate complete code listing
pcopy tree > project-snapshot.txt
```

## 🚀 Building Standalone Executable

Want to create your own standalone executable?

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
python -m PyInstaller --onefile --console --name pcopy pcopy.py

# Output: dist/pcopy.exe (Windows) or dist/pcopy (Linux/Mac)
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 Changelog

See [Releases](https://github.com/abbasahsan1/Pcopy/releases) for version history.

## 🐛 Troubleshooting

**"No text files found"**
- Check your `.pcopyignore` patterns
- Verify you're in the correct directory

**Clipboard not working on Linux**
```bash
sudo apt-get install xclip
```

**Permission errors**
- Run with appropriate permissions
- Check file/folder access rights

## ⭐ Star this project

If you find pcopy useful, please give it a star on GitHub!

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python 3.10
- [pyperclip](https://github.com/asweigart/pyperclip) for clipboard operations
- [pathspec](https://github.com/cpburnz/python-pathspec) for pattern matching
- [PyInstaller](https://www.pyinstaller.org/) for executable creation

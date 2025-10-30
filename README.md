# pcopy - Project Copy Tool

A cross-platform command-line tool that reads all text-based files in a specified folder, merges them into a single file called `PROMPT.txt`, and copies its entire content to the clipboard.

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

Perfect for:
- Preparing code context for LLMs (ChatGPT, Claude, etc.)
- Creating project snapshots
- Code reviews and sharing
- Documentation generation
- Quick project overviews

## License

MIT License

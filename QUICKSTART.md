# pcopy - Quick Start Guide

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run pcopy

**Option A: Using Python directly**
```bash
python pcopy.py [tree] [path]
```

**Option B: Using the batch file (Windows)**
```bash
pcopy.bat [tree] [path]
```

**Option C: Add to PATH for global access**

#### Windows (PowerShell as Administrator):
```powershell
# Method 1: Copy to Python Scripts folder
copy pcopy.py "$env:APPDATA\Python\Python311\Scripts\"
copy pcopy.bat "$env:APPDATA\Python\Python311\Scripts\"

# Method 2: Add current directory to PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newPath = "$currentPath;X:\Pcopy"
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")
```

After adding to PATH, restart your terminal and use:
```bash
pcopy [tree] [path]
```

#### Linux/Mac/WSL:
```bash
# Make executable
chmod +x pcopy.py

# Create symlink
sudo ln -s $(pwd)/pcopy.py /usr/local/bin/pcopy

# Or add alias to ~/.bashrc or ~/.zshrc
echo 'alias pcopy="python3 /path/to/pcopy/pcopy.py"' >> ~/.bashrc
source ~/.bashrc
```

## 📖 Usage Examples

### Basic Usage
```bash
# Merge files in current directory
pcopy

# Merge files in specific directory
pcopy C:\Projects\MyApp

# Include file tree visualization
pcopy tree

# Both tree and custom path
pcopy tree C:\Projects\MyApp
```

### Real-World Examples

**1. Prepare code for ChatGPT/Claude:**
```bash
cd my-python-project
pcopy tree
# Now paste clipboard content into your AI chat!
```

**2. Share project structure with team:**
```bash
pcopy tree C:\Work\api-server
# PROMPT.txt contains complete project overview
```

**3. Code review preparation:**
```bash
pcopy C:\Projects\feature-branch
# Share PROMPT.txt with reviewers
```

## 🔧 Configuration

### Creating a .pcopyignore file

Create a `.pcopyignore` file in your project root:

```bash
# Copy the sample
copy .pcopyignore.sample .pcopyignore

# Or create manually
notepad .pcopyignore
```

Example `.pcopyignore`:
```
# Ignore build outputs
build/
dist/
*.exe

# Ignore dependencies
node_modules/
__pycache__/

# Ignore sensitive files
.env
secrets.json
*.key

# But keep this specific file
!important-config.yaml
```

### Supported File Types

**Automatically included:**
- Source code: `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.cs`, `.go`, `.rs`, etc.
- Config files: `.json`, `.yaml`, `.xml`, `.ini`, `.conf`, `.toml`
- Documentation: `.md`, `.txt`, `.rst`
- Web files: `.html`, `.css`, `.scss`
- Scripts: `.sh`, `.bat`, `.ps1`

**Automatically excluded:**
- Binary files: `.exe`, `.dll`, `.so`, `.zip`, `.rar`
- Media files: `.jpg`, `.png`, `.mp4`, `.mp3`
- Large files: > 5 MB
- Hidden folders: `.git`, `node_modules`, `__pycache__`

## 🐛 Troubleshooting

### "pyperclip not installed"
```bash
pip install pyperclip
```

### "pathspec not installed"
```bash
pip install pathspec
```

### Clipboard not working on Linux
```bash
# Install xclip or xsel
sudo apt-get install xclip
# or
sudo apt-get install xsel
```

### "No text files found"
- Check your `.pcopyignore` patterns
- Verify you're in the correct directory
- Ensure files have recognized text extensions

### Large output warning
If output is very large (>10 MB), clipboard copy might fail. The file is still saved as `PROMPT.txt`.

## 💡 Tips & Tricks

### 1. Quick LLM Context
```bash
# Before asking AI for help
pcopy tree
# Paste clipboard into AI chat with your question
```

### 2. Project Documentation
```bash
# Generate project snapshot
pcopy tree > project-snapshot.txt
```

### 3. Selective File Collection
Create `.pcopyignore` to exclude:
- Test files: `**/test_*.py`
- Docs: `docs/`
- Only include src: Add `*` then `!src/`

### 4. Multiple Projects
```bash
# Compare two projects
pcopy tree C:\Project1
rename PROMPT.txt project1.txt
pcopy tree C:\Project2
rename PROMPT.txt project2.txt
```

## 📊 Output Format

```
==================================================================
📁 FILE TREE
==================================================================

project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── README.md
└── requirements.txt

==================================================================
📄 FILE CONTENTS
==================================================================

Filename: src/main.py
Content:
{
def main():
    print("Hello World")
}

------------------------------------------------------------------

Filename: README.md
Content:
{
# My Project
...
}

------------------------------------------------------------------
```

## 🔄 Updates & Maintenance

Keep pcopy up to date:
```bash
# Update dependencies
pip install --upgrade pyperclip pathspec

# Check Python version (requires 3.7+)
python --version
```

## 📝 License

MIT License - Free to use and modify!

---

**Need help?** Check the full documentation in `README.md` or create an issue on GitHub.

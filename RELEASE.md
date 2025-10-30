# Release Notes

Use this template for creating GitHub releases.

---

## pcopy v1.0.0 - Initial Release 🎉

**Release Date:** October 30, 2025

> Merge all text files in a folder into one file and copy to clipboard.  
> Perfect for preparing code context for AI assistants!

### 📥 Download

**Windows (No Python Required):**
- [pcopy-v1.0.0-windows-x64.zip](https://github.com/abbasahsan1/Pcopy/releases/download/v1.0.0/pcopy-v1.0.0-windows-x64.zip) (5.2 MB)

**Python Script (All Platforms):**
```bash
git clone https://github.com/abbasahsan1/Pcopy.git
pip install -r requirements.txt
```

### 🚀 Quick Start

1. Download and extract the ZIP
2. Run: `pcopy.exe tree`
3. Done! Content copied to clipboard ✅

**No installation needed!**

### ✨ Features

- 🗂️ **Recursive file gathering** - Collects all text files
- 🌳 **File tree visualization** - Optional ASCII tree
- 📋 **Auto clipboard copy** - Instant copy to clipboard
- 🚫 **Smart filtering** - .gitignore-style patterns
- 🔍 **Binary detection** - Automatically skips binary files
- 🌐 **Cross-platform** - Windows, Linux, Mac, WSL
- 📝 **Multiple encodings** - UTF-8, UTF-16, BOM support
- ⚡ **No dependencies** - Standalone executable

### 💻 Usage

```bash
pcopy              # Current directory
pcopy tree         # With file tree
pcopy C:\Project   # Specific path
```

### 🎯 Use Cases

**Prepare Context for AI:**
```bash
cd my-project
pcopy tree
# Paste into ChatGPT/Claude!
```

**Code Reviews:**
```bash
pcopy tree feature-branch/
# Share PROMPT.txt with team
```

**Project Documentation:**
```bash
pcopy tree
# Complete project overview
```

### 📦 What's Included

- `pcopy.exe` (5.4 MB) - Standalone executable
- `README.md` - Full documentation
- `QUICKSTART.md` - Getting started guide
- `.pcopyignore.sample` - Example patterns
- `QUICK_README.txt` - Simple instructions

### 🚫 .pcopyignore Support

Create `.pcopyignore` file with gitignore syntax:

```
build/
dist/
node_modules/
*.log
.env
```

**Auto-ignored:** `.git/`, `__pycache__/`, binary files, files >5MB

### 🐛 Known Issues

- Files >5MB are skipped (configurable in code)
- Linux clipboard requires xclip/xsel
- Very large projects may produce large output

### 📊 Technical Details

- **Platform:** Windows x64 (Python script: cross-platform)
- **Size:** 5.4 MB
- **Python:** 3.10 (not required for .exe)
- **License:** MIT

### 🆕 What's New in v1.0.0

- ✅ Initial release
- ✅ Standalone Windows executable
- ✅ Cross-platform Python script
- ✅ File tree visualization
- ✅ Smart filtering with .pcopyignore
- ✅ Multiple encoding support
- ✅ Automatic clipboard copy
- ✅ Binary file detection
- ✅ Default ignore patterns

### 🤝 Contributing

Contributions welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### 📄 License

MIT License - Free to use and modify!

### ⭐ Star if useful!

**Full Changelog:** https://github.com/abbasahsan1/Pcopy/commits/v1.0.0

---

## Template for Future Releases

```markdown
## pcopy vX.Y.Z - Release Title

**Release Date:** Month DD, YYYY

### 🆕 What's New

- Feature 1
- Feature 2
- Bug fix 1

### 🔧 Changes

- Change 1
- Change 2

### 🐛 Bug Fixes

- Fix 1
- Fix 2

### 📥 Download

**Windows:**
- [pcopy-vX.Y.Z-windows-x64.zip](link)

### 📊 Technical Details

- **Size:** X.X MB
- **Python:** 3.X

### ⬆️ Upgrade Instructions

For existing users:
1. Download new version
2. Replace old executable
3. No configuration changes needed

**Full Changelog:** https://github.com/abbasahsan1/Pcopy/compare/vX.Y.Z-1...vX.Y.Z
```

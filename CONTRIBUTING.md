# Contributing to pcopy

Thank you for your interest in contributing to pcopy! This document provides guidelines and instructions for contributors.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Building Executable](#building-executable)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)
- [Publishing Release](#publishing-release)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- pip (Python package manager)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/Pcopy.git
cd Pcopy
```

3. Add upstream remote:
```bash
git remote add upstream https://github.com/abbasahsan1/Pcopy.git
```

## Development Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Development Tools

```bash
pip install pyinstaller twine wheel
```

### 3. Test the Script

```bash
python pcopy.py tree
```

## Building Executable

### Windows

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone executable
python -m PyInstaller --onefile --console --name pcopy pcopy.py

# Test the executable
.\dist\pcopy.exe tree
```

### Linux/Mac

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone executable
python -m PyInstaller --onefile --console --name pcopy pcopy.py

# Make executable
chmod +x dist/pcopy

# Test the executable
./dist/pcopy tree
```

### Automated Build Script (Windows)

```powershell
.\build_standalone.ps1
```

This script will:
- Check dependencies
- Build executable
- Run tests
- Create release package

## Testing

### Manual Testing

Test basic functionality:

```bash
# Test current directory
python pcopy.py

# Test with tree
python pcopy.py tree

# Test specific path
python pcopy.py C:\TestProject

# Test with .pcopyignore
# Create .pcopyignore file first
python pcopy.py tree
```

### Test Executable

```bash
# Windows
.\dist\pcopy.exe tree

# Linux/Mac
./dist/pcopy tree
```

### Test Cases to Cover

- ✅ Empty directory
- ✅ Directory with only binary files
- ✅ Directory with mixed files
- ✅ Large project (100+ files)
- ✅ Files with different encodings (UTF-8, UTF-16)
- ✅ .pcopyignore patterns
- ✅ Clipboard functionality
- ✅ Permission errors
- ✅ Invalid paths

## Code Style

### Python Style Guidelines

- Follow PEP 8
- Use type hints where possible
- Add docstrings for functions
- Keep functions focused and small
- Use meaningful variable names

### Example

```python
def is_text_file(file_path: Path) -> bool:
    """
    Determine if a file is text-based.
    
    Args:
        file_path: Path to the file to check
        
    Returns:
        True if file is text, False otherwise
    """
    # Implementation
    pass
```

### File Organization

```
pcopy/
├── pcopy.py              # Main script
├── requirements.txt      # Dependencies
├── setup.py             # PyPI setup
├── README.md            # Main documentation
├── QUICKSTART.md        # Quick start guide
├── CONTRIBUTING.md      # This file
├── LICENSE              # MIT License
├── .gitignore           # Git ignore patterns
└── .pcopyignore.sample  # Example ignore file
```

## Submitting Changes

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Changes

- Write clear, concise code
- Add comments for complex logic
- Update documentation if needed
- Test your changes thoroughly

### 3. Commit Changes

```bash
git add .
git commit -m "Description of changes"
```

**Commit Message Format:**
```
[type]: Brief description

Detailed explanation if needed

Fixes #issue-number (if applicable)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add support for custom output filename

- Allow users to specify output file name via --output flag
- Update documentation
- Add tests for new functionality

Fixes #42
```

### 4. Push Changes

```bash
git push origin feature/your-feature-name
```

### 5. Create Pull Request

1. Go to GitHub repository
2. Click "New Pull Request"
3. Select your branch
4. Fill in PR template:
   - Description of changes
   - Testing done
   - Related issues
5. Submit PR

### PR Guidelines

- Provide clear description
- Link related issues
- Include screenshots if UI changes
- Ensure tests pass
- Be responsive to feedback

## Publishing Release

### For Maintainers

#### 1. Update Version

Update version in `pcopy.py`:
```python
Version: 1.1.0
```

#### 2. Update Changelog

Create release notes in `RELEASE.md`

#### 3. Build Executable

```bash
# Windows
python -m PyInstaller --onefile --console --name pcopy pcopy.py

# Create release package
Compress-Archive -Path release\* -DestinationPath pcopy-v1.1.0-windows-x64.zip
```

#### 4. Test Release Package

- Test on clean machine without Python
- Verify all functionality works
- Check documentation is included

#### 5. Create Git Tag

```bash
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0
```

#### 6. Create GitHub Release

1. Go to Releases → Create new release
2. Tag: `v1.1.0`
3. Title: `pcopy v1.1.0`
4. Description: Copy from `RELEASE.md`
5. Upload: `pcopy-v1.1.0-windows-x64.zip`
6. Publish release

#### 7. Publish to PyPI (Optional)

```bash
# Build distribution
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

## Adding to PATH (Windows)

For testing during development:

```powershell
# Run the included script
.\add_to_path.ps1

# Or manually add to PATH
$env:Path += ";$PWD"
[Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
```

## Project Structure

```
pcopy/
├── pcopy.py                    # Main application
├── requirements.txt            # Python dependencies
├── setup.py                   # PyPI configuration
├── pcopy.spec                 # PyInstaller spec
├── pcopy.bat                  # Windows launcher
├── add_to_path.ps1           # PATH installer
├── build_standalone.ps1       # Build automation
├── .pcopyignore.sample       # Example ignore file
├── README.md                  # Main documentation
├── QUICKSTART.md             # Quick start guide
├── CONTRIBUTING.md           # This file
├── LICENSE                    # MIT License
└── .gitignore                # Git ignore patterns
```

## Common Issues

### Import Errors

```bash
pip install -r requirements.txt
```

### PyInstaller Not Found

```bash
pip install pyinstaller
```

### Clipboard Not Working (Linux)

```bash
sudo apt-get install xclip
# or
sudo apt-get install xsel
```

### Permission Denied

```bash
# Linux/Mac
chmod +x pcopy.py
```

## Questions?

- **Issues:** https://github.com/abbasahsan1/Pcopy/issues
- **Discussions:** https://github.com/abbasahsan1/Pcopy/discussions

## Code of Conduct

Be respectful, inclusive, and professional. We're all here to build something useful together.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to pcopy!** 🎉

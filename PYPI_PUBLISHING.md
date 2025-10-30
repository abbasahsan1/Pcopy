# Publishing pcopy to PyPI

This guide explains how to publish pcopy to the Python Package Index (PyPI).

## Prerequisites

1. **PyPI Account:**
   - Create account at: https://pypi.org/account/register/
   - Verify your email
   - Optional: Set up 2FA for security

2. **Test PyPI Account (Optional but Recommended):**
   - Create account at: https://test.pypi.org/account/register/
   - Use this for testing before real release

3. **API Tokens:**
   - Go to Account Settings → API tokens
   - Create token with scope "Entire account" or specific to pcopy-tool
   - **Save the token** - you can't see it again!

## Setup

### 1. Install Required Tools

```bash
pip install build twine
```

### 2. Configure PyPI Credentials

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

**Security Note:** Keep this file private! Add to .gitignore

## Building the Package

### 1. Clean Previous Builds

```bash
# Remove old builds
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
```

### 2. Build Distributions

```bash
# Build both source distribution and wheel
python -m build

# Or manually:
python setup.py sdist bdist_wheel
```

**Output:**
```
dist/
├── pcopy_tool-1.0.0.tar.gz       # Source distribution
└── pcopy_tool-1.0.0-py3-none-any.whl  # Wheel (binary)
```

### 3. Verify Build

```bash
# Check contents of wheel
python -m zipfile -l dist/pcopy_tool-1.0.0-py3-none-any.whl

# Check package metadata
python -m twine check dist/*
```

## Testing on Test PyPI

### 1. Upload to Test PyPI

```bash
python -m twine upload --repository testpypi dist/*
```

### 2. Test Installation

```bash
# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pcopy-tool

# Test the command
pcopy --help
pcopy tree
```

### 3. Uninstall Test

```bash
pip uninstall pcopy-tool
```

## Publishing to PyPI

### 1. Final Checks

- [ ] Version number updated in `pyproject.toml` and `pcopy.py`
- [ ] README.md is current
- [ ] CHANGELOG updated
- [ ] Tests pass
- [ ] Package builds without errors
- [ ] Test installation works
- [ ] Git tag created: `git tag v1.0.0`

### 2. Upload to PyPI

```bash
python -m twine upload dist/*
```

**You'll see:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading pcopy_tool-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 kB • 00:01
Uploading pcopy_tool-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.8/18.8 kB • 00:01

View at:
https://pypi.org/project/pcopy-tool/1.0.0/
```

### 3. Verify Publication

Visit: https://pypi.org/project/pcopy-tool/

### 4. Test Installation from PyPI

```bash
# In a fresh environment
pip install pcopy-tool

# Test
pcopy --help
pcopy tree
```

## Post-Publication

### 1. Tag Release on GitHub

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 2. Create GitHub Release

- Go to: https://github.com/abbasahsan1/Pcopy/releases
- Create new release with tag `v1.0.0`
- Add release notes from `RELEASE.md`
- Mention PyPI availability

### 3. Update README

Add PyPI badges:

```markdown
[![PyPI version](https://badge.fury.io/py/pcopy-tool.svg)](https://badge.fury.io/py/pcopy-tool)
[![PyPI downloads](https://img.shields.io/pypi/dm/pcopy-tool.svg)](https://pypi.org/project/pcopy-tool/)
```

## Updating the Package

### For New Versions:

1. **Update version number:**
   - `pyproject.toml`: `version = "1.0.1"`
   - `pcopy.py`: `Version: 1.0.1`

2. **Update CHANGELOG:**
   - Document changes in `RELEASE.md`

3. **Commit changes:**
   ```bash
   git add .
   git commit -m "chore: bump version to 1.0.1"
   git push
   ```

4. **Clean and rebuild:**
   ```bash
   Remove-Item -Recurse -Force dist, build, *.egg-info
   python -m build
   ```

5. **Upload:**
   ```bash
   python -m twine upload dist/*
   ```

6. **Tag release:**
   ```bash
   git tag -a v1.0.1 -m "Release version 1.0.1"
   git push origin v1.0.1
   ```

## Troubleshooting

### "File already exists"

You can't overwrite existing versions. Increment version number.

### "Invalid credentials"

- Check your API token in `~/.pypirc`
- Regenerate token if needed
- Use `__token__` as username

### "Twine not found"

```bash
pip install twine
```

### "Package name already taken"

The name `pcopy-tool` should be available. If not, choose different name in `pyproject.toml`.

### "README rendering issues"

```bash
# Validate README
python -m twine check dist/*

# Check on Test PyPI first
```

## Package Statistics

After publishing, view stats at:
- **PyPI Page:** https://pypi.org/project/pcopy-tool/
- **Download Stats:** https://pypistats.org/packages/pcopy-tool

## Best Practices

1. **Always test on Test PyPI first**
2. **Use semantic versioning:** MAJOR.MINOR.PATCH
3. **Tag all releases in Git**
4. **Document changes in RELEASE.md**
5. **Keep dependencies minimal**
6. **Test installation in clean environment**
7. **Use API tokens, not passwords**
8. **Never commit tokens to Git**

## Automated Publishing (GitHub Actions)

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Add `PYPI_API_TOKEN` to GitHub Secrets.

## Quick Reference

```bash
# Build
python -m build

# Check
python -m twine check dist/*

# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install pcopy-tool
```

## Success!

Once published, users can install with:

```bash
pip install pcopy-tool
```

And use:

```bash
pcopy tree
```

🎉 **Your package is now available to millions of Python users!**

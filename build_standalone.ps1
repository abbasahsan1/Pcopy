# Build Standalone Executable for pcopy
# This script creates a single .exe file that works without Python installed

Write-Host "🔨 Building pcopy standalone executable..." -ForegroundColor Cyan
Write-Host ""

# Step 1: Check if PyInstaller is installed
Write-Host "Checking PyInstaller..." -ForegroundColor Yellow
python -c "import PyInstaller" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing PyInstaller..." -ForegroundColor Yellow
    pip install pyinstaller
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install PyInstaller" -ForegroundColor Red
        exit 1
    }
}
Write-Host "✅ PyInstaller ready" -ForegroundColor Green
Write-Host ""

# Step 2: Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Recurse -Force build }
if (Test-Path "dist") { Remove-Item -Recurse -Force dist }
Write-Host "✅ Cleaned" -ForegroundColor Green
Write-Host ""

# Step 3: Build executable
Write-Host "Building executable (this may take 30-60 seconds)..." -ForegroundColor Yellow
pyinstaller --onefile --console --name pcopy pcopy.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Build failed" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Build successful" -ForegroundColor Green
Write-Host ""

# Step 4: Test the executable
Write-Host "Testing executable..." -ForegroundColor Yellow
$testDir = ".\test_build_$(Get-Random)"
New-Item -ItemType Directory -Path $testDir | Out-Null
Set-Content -Path "$testDir\test.txt" -Value "Test content"

.\dist\pcopy.exe $testDir | Out-Null
if ($LASTEXITCODE -eq 0 -and (Test-Path "$testDir\PROMPT.txt")) {
    Write-Host "✅ Executable works correctly" -ForegroundColor Green
    Remove-Item -Recurse -Force $testDir
} else {
    Write-Host "⚠️  Executable test failed" -ForegroundColor Yellow
    Remove-Item -Recurse -Force $testDir
}
Write-Host ""

# Step 5: Get file size
$exeSize = (Get-Item "dist\pcopy.exe").Length / 1MB
Write-Host "📦 Executable size: $([math]::Round($exeSize, 2)) MB" -ForegroundColor Cyan
Write-Host ""

# Step 6: Create release package
Write-Host "Creating release package..." -ForegroundColor Yellow
$releaseDir = ".\release"
if (Test-Path $releaseDir) { Remove-Item -Recurse -Force $releaseDir }
New-Item -ItemType Directory -Path $releaseDir | Out-Null

Copy-Item "dist\pcopy.exe" $releaseDir\
Copy-Item "README.md" $releaseDir\
Copy-Item ".pcopyignore.sample" $releaseDir\
Copy-Item "QUICKSTART.md" $releaseDir\

# Create simple README for end users
$userReadme = @"
pcopy v1.0.0 - Standalone Release

QUICK START:
1. Copy pcopy.exe to any folder
2. Add that folder to your PATH (optional)
3. Run: pcopy tree

USAGE:
  pcopy                    - Merge files in current directory
  pcopy tree              - Include file tree visualization
  pcopy C:\MyProject      - Specific directory
  pcopy tree C:\MyProject - Both options

No Python or dependencies required!

Full documentation: See README.md and QUICKSTART.md

"@

Set-Content -Path "$releaseDir\QUICK_README.txt" -Value $userReadme

# Create zip file
$zipName = "pcopy-v1.0.0-windows-x64.zip"
if (Test-Path $zipName) { Remove-Item $zipName }
Compress-Archive -Path "$releaseDir\*" -DestinationPath $zipName

Write-Host "✅ Release package created: $zipName" -ForegroundColor Green
Write-Host ""

# Summary
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "🎉 Build Complete!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "Output files:" -ForegroundColor White
Write-Host "  📄 dist\pcopy.exe                  - Standalone executable" -ForegroundColor Gray
Write-Host "  📦 $zipName  - Release package" -ForegroundColor Gray
Write-Host ""
Write-Host "Test the executable:" -ForegroundColor White
Write-Host "  .\dist\pcopy.exe tree" -ForegroundColor Gray
Write-Host ""
Write-Host "Share with users:" -ForegroundColor White
Write-Host "  Send them $zipName" -ForegroundColor Gray
Write-Host "  No Python installation needed!" -ForegroundColor Gray
Write-Host ""

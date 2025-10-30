# Test Script for pcopy

Write-Host "🧪 Testing pcopy installation..." -ForegroundColor Cyan
Write-Host ""

# Test 1: Check Python
Write-Host "Test 1: Python availability" -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python not found!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Python OK" -ForegroundColor Green
Write-Host ""

# Test 2: Check dependencies
Write-Host "Test 2: Dependencies" -ForegroundColor Yellow
python -c "import pyperclip; import pathspec; print('✅ All dependencies installed')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Dependencies missing! Run: pip install -r requirements.txt" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Test 3: Check pcopy script
Write-Host "Test 3: pcopy.py exists and is readable" -ForegroundColor Yellow
if (Test-Path "pcopy.py") {
    Write-Host "✅ pcopy.py found" -ForegroundColor Green
} else {
    Write-Host "❌ pcopy.py not found!" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Test 4: Create test directory and run pcopy
Write-Host "Test 4: Running pcopy on test data" -ForegroundColor Yellow
$testDir = ".\test_temp_$(Get-Random)"
New-Item -ItemType Directory -Path $testDir | Out-Null
Set-Content -Path "$testDir\test1.txt" -Value "Hello from test file 1"
Set-Content -Path "$testDir\test2.py" -Value "print('Test Python file')"
Set-Content -Path "$testDir\README.md" -Value "# Test README"

python pcopy.py tree $testDir
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ pcopy executed successfully" -ForegroundColor Green
    
    # Check if PROMPT.txt was created
    if (Test-Path "$testDir\PROMPT.txt") {
        Write-Host "✅ PROMPT.txt created" -ForegroundColor Green
        
        # Check if content looks correct
        $content = Get-Content "$testDir\PROMPT.txt" -Raw
        if ($content -match "FILE TREE" -and $content -match "FILE CONTENTS") {
            Write-Host "✅ Output format is correct" -ForegroundColor Green
        } else {
            Write-Host "⚠️  Output format might be incorrect" -ForegroundColor Yellow
        }
    } else {
        Write-Host "❌ PROMPT.txt not created" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "❌ pcopy execution failed" -ForegroundColor Red
    exit 1
}

# Cleanup
Remove-Item -Recurse -Force $testDir
Write-Host ""

# Summary
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "🎉 All tests passed! pcopy is ready to use!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "Quick start:" -ForegroundColor White
Write-Host "  python pcopy.py tree          # Current directory with tree" -ForegroundColor Gray
Write-Host "  python pcopy.py C:\MyProject  # Specific directory" -ForegroundColor Gray
Write-Host "  pcopy.bat tree                # Using batch file" -ForegroundColor Gray
Write-Host ""
Write-Host "Documentation: README.md, QUICKSTART.md" -ForegroundColor White

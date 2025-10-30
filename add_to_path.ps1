# Add pcopy to Windows PATH
Write-Host "Adding pcopy to Windows PATH..." -ForegroundColor Cyan
Write-Host ""

$pcopyDir = "X:\Pcopy"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($currentPath -like "*$pcopyDir*") {
    Write-Host "[OK] pcopy is already in PATH!" -ForegroundColor Green
    exit 0
}

$newPath = "$currentPath;$pcopyDir"
[Environment]::SetEnvironmentVariable("Path", $newPath, "User")
Write-Host "[OK] Successfully added to PATH" -ForegroundColor Green
Write-Host ""
Write-Host "[!] Restart your terminal to use: pcopy tree" -ForegroundColor Yellow

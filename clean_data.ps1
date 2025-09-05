# PowerShell script to clean CSV data
Write-Host "🧹 Starting CSV data cleanup..." -ForegroundColor Green

# Activate virtual environment if it exists
if (Test-Path "dash_env\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & "dash_env\Scripts\Activate.ps1"
}

# Run Django management command
Write-Host "Running Django clean command..." -ForegroundColor Yellow
python manage.py clean_csv_files --force

Write-Host "🎉 Cleanup completed!" -ForegroundColor Green
Read-Host "Press Enter to continue"

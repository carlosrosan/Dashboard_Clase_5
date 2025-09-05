@echo off
echo Cleaning CSV data...
echo.

REM Activate virtual environment if it exists
if exist "dash_env\Scripts\activate.bat" (
    echo Activating virtual environment...
    call dash_env\Scripts\activate.bat
)

REM Run Django management command
echo Running Django clean command...
python manage.py clean_csv_files --force

echo.
echo Cleanup completed!
pause

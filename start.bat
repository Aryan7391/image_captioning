@echo off
echo ========================================
echo         CaptionNet - Starting...
echo ========================================
echo.

:: Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.8+ from https://python.org
    pause
    exit
)

:: Check if setup has been run
if not exist "model\vocab.pkl" (
    echo WARNING: Setup not complete!
    echo Please run setup.bat first
    pause
    exit
)

echo Opening browser...
start http://localhost:5000

echo Starting server...
echo Press Ctrl+C to stop
echo.
python app.py
pause
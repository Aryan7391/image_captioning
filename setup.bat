@echo off
echo ========================================
echo     CaptionNet - First Time Setup
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

echo ✓ Python found
echo.
echo Starting setup...
echo.

python setup.py

echo.
echo ========================================
echo     Setup Complete!
echo     Run start.bat to launch the app
echo ========================================
pause
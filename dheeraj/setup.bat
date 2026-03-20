@echo off
REM ==========================================
REM Portfolio Website - Setup Script (Windows)
REM ==========================================

echo.
echo ======================================================
echo  Portfolio Website Setup
echo ======================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [✓] Python detected
echo.

REM Create virtual environment
echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo [✓] Virtual environment created
echo.

REM Activate virtual environment
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
echo [✓] Virtual environment activated
echo.

REM Install requirements
echo [3/4] Installing dependencies...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [✓] Dependencies installed
echo.

REM Ready to run
echo [4/4] Setup complete!
echo.
echo ======================================================
echo  TO START THE SERVER:
echo ======================================================
echo.
echo 1. Make sure you're in the project directory
echo 2. Run: python app.py
echo 3. Open your browser to: http://localhost:5000
echo.
echo ======================================================
echo  TEST CREDENTIALS:
echo ======================================================
echo.
echo Email: test@example.com
echo Password: password123 (register first)
echo.
echo ======================================================
echo.
pause

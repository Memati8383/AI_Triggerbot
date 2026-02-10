@echo off
cls
echo.
echo ========================================
echo   AI TRIGGERBOT - CLEAN EDITION
echo ========================================
echo.
echo [1/3] Checking virtual environment...

if not exist "venv\" (
    echo [!] Virtual environment not found!
    echo [!] Creating virtual environment...
    python -m venv venv
    echo [+] Virtual environment created
)

echo [+] Virtual environment found
echo.
echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat

echo [+] Virtual environment activated
echo.
echo [3/3] Starting AI Triggerbot...
echo.
echo ========================================
echo   CONTROLS:
echo   F2  - Toggle On/Off
echo   F3  - Confidence +0.05
echo   F4  - Confidence -0.05
echo   F9  - Toggle Debug Window
echo   F10 - Cycle Profile
echo ========================================
echo.

python app.py

if errorlevel 1 (
    echo.
    echo [!] Error occurred!
    echo [!] Check if all dependencies are installed:
    echo     pip install torch torchvision ultralytics
    echo     pip install mss numpy pywin32 opencv-python
    echo.
)

pause

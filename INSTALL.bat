@echo off
cls
echo.
echo ========================================
echo   AI TRIGGERBOT - INSTALLATION
echo ========================================
echo.
echo [1/4] Creating virtual environment...
python -m venv venv
echo [+] Virtual environment created
echo.

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
echo [+] Activated
echo.

echo [3/4] Installing dependencies...
echo     This may take a few minutes...
echo.
pip install torch torchvision ultralytics
pip install mss numpy pywin32 opencv-python
echo.
echo [+] Dependencies installed
echo.

echo [4/4] Verifying installation...
python -c "import torch; import cv2; import mss; print('[+] All packages OK')"
echo.

echo ========================================
echo   INSTALLATION COMPLETE!
echo ========================================
echo.
echo Next steps:
echo   1. Place yolo11s.pt in models/ folder
echo   2. Run START.bat to launch
echo.
pause

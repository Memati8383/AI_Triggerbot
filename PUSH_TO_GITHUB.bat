@echo off
cls
echo.
echo ========================================
echo   GITHUB'A PUSH ETME
echo ========================================
echo.

echo [1/5] Git durumunu kontrol ediliyor...
git status
echo.

echo [2/5] Tum degisiklikleri ekleniyor...
git add .
echo.

echo [3/5] Commit mesaji giriniz:
set /p commit_msg="Mesaj: "
echo.

echo [4/5] Commit yapiliyor...
git commit -m "%commit_msg%"
echo.

echo [5/5] GitHub'a push ediliyor...
git push origin main
echo.

if errorlevel 1 (
    echo.
    echo [!] Hata olustu!
    echo [!] Ilk kez push ediyorsaniz:
    echo     git remote add origin https://github.com/Memati8383/AI_Triggerbot.git
    echo     git branch -M main
    echo     git push -u origin main
    echo.
) else (
    echo.
    echo ========================================
    echo   BASARIYLA PUSH EDILDI!
    echo ========================================
    echo.
)

pause

@echo off
chcp 65001 >nul
title 小說翻譯器 - 本地伺服器

echo ================================================
echo   小說翻譯器 本地伺服器
echo   關閉請直接關閉此視窗
echo ================================================
echo.

:: 檢查 python-3.13.11-embed-amd64 資料夾是否存在
if not exist "%~dp0python-3.13.11-embed-amd64\python.exe" (
    echo [錯誤] 找不到 python-3.13.11-embed-amd64\python.exe
    echo 請確認資料夾結構如下：
    echo.
    echo   翻譯軟體\
    echo   ├── python-3.13.11-embed-amd64\
    echo   │   └── python.exe  ^← 需要這個
    echo   ├── server.py
    echo   └── 啟動伺服器.bat
    echo.
    pause
    exit /b 1
)

:: 檢查 server.py 是否存在
if not exist "%~dp0server.py" (
    echo [錯誤] 找不到 server.py
    echo 請確認 server.py 和此 bat 檔在同一個資料夾
    echo.
    pause
    exit /b 1
)

:: 啟動伺服器
"%~dp0python-3.13.11-embed-amd64\python.exe" "%~dp0server.py"
pause

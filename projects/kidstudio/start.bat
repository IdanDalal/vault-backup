@echo off
rem Studio: double-click this. Starts the page server and opens the page full screen.
rem Close the black window to stop the server. Alt+F4 closes the full-screen browser.
cd /d "%~dp0"
rem If an old server still holds port 8787 (a black window left open, or a test run), stop it first.
for /f "tokens=5" %%p in ('netstat -ano ^| findstr /r /c:":8787 .*LISTENING"') do taskkill /pid %%p /f >nul 2>&1
start "Studio server" venv\Scripts\python.exe server.py
timeout /t 4 /nobreak >nul
start "" msedge --new-window --start-fullscreen http://127.0.0.1:8787

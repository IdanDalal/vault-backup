@echo off
setlocal

rem ===========================================================
rem  weekly-archive.bat
rem  Dated full copies to the external drive.
rem  No service, no scheduler, no Microsoft feature to fight.
rem    RUN:     double-click this file
rem    RESTORE: open the dated folder, copy the file back
rem ===========================================================

rem --- 1. destination drive letter
set DRIVE=G:
set ROOT=%DRIVE%\Backup

rem --- 2. copy flags. For a PREVIEW that writes nothing,
rem        comment out the first line, uncomment the second.
set FLAGS=/E /R:1 /W:1 /XJ /NP
rem set FLAGS=/E /R:1 /W:1 /XJ /L

if not exist "%DRIVE%\." (
  echo.
  echo   Drive %DRIVE% is not there.
  echo   Plug it in, or change DRIVE at the top of this file.
  echo.
  pause
  exit /b 1
)

for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set STAMP=%%d
set DEST=%ROOT%\%STAMP%

echo.
echo   Destination: %DEST%
echo.

robocopy "%USERPROFILE%\Documents" "%DEST%\Documents" %FLAGS%
robocopy "%USERPROFILE%\Desktop"   "%DEST%\Desktop"   %FLAGS%
robocopy "%USERPROFILE%\Pictures"  "%DEST%\Pictures"  %FLAGS%

rem --- 3. game saves: paste the folder from A4, then delete the rem
rem robocopy "PASTE_SAVE_FOLDER_HERE" "%DEST%\Saves" %FLAGS%

echo.
echo   Finished. Scan the output above for a non-zero FAILED column.
echo   Folder: %DEST%
echo.
echo   Retention: delete whole dated folders in Explorer when the
echo   drive fills. Nothing else points at them.
echo.
pause

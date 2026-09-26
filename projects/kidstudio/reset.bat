@echo off
rem Empties the girls' word logs and output folders. Run after a test run-through, before a real session.
cd /d "%~dp0"
type nul > log\K.txt
type nul > log\D.txt
del /q out\K\* 2>nul
del /q out\D\* 2>nul
echo Studio: word logs and outputs cleared.
pause

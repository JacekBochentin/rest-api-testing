@echo off
REM Skrypt do automatycznej instalacji i uruchomienia projektu (Windows)

REM 1. Instalacja zależności Node.js
echo Installing Node.js dependencies...
npm install express

REM 2. Instalacja zależności Python
echo Installing Python dependencies...
pip install robotframework requests

REM 3. Uruchomienie REST API w tle
echo Starting REST API...
start /B node rest_api.js

REM Poczekaj, aż API się uruchomi
timeout /t 2 >nul

REM 4. Uruchomienie testów
echo Running tests...
robot test_rest_api.robot
@echo off
REM Script for automatic installation and running the project (Windows)

REM 1. Install Node.js dependencies
echo Installing Node.js dependencies...
npm install express  REM Install the Express.js library using npm (Node.js package manager)

REM 2. Install Python dependencies
echo Installing Python dependencies...
pip install robotframework requests  REM Install Robot Framework and requests library using pip (Python package manager)

REM 3. Run REST API in the background
echo Starting REST API...
start /B node rest_api.js  REM Start the REST API server in the background using the 'start /B' command

REM Wait for the API to initialize
timeout /t 2 >nul  REM Wait for 2 seconds to give the API time to initialize

REM 4. Run the tests
echo Running tests...
robot test_rest_api.robot  REM Run the Robot Framework tests using the 'robot' command, targeting the test file 'test_rest_api.robot'

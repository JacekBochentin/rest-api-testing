#!/bin/bash

# Script for automatic installation and running the project

# 1. Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install express  # Install the Express.js library using npm (Node.js package manager)

# 2. Install Python dependencies
echo "Installing Python dependencies..."
pip install robotframework requests  # Install Robot Framework and requests library using pip (Python package manager)

# 3. Run REST API in the background
echo "Starting REST API..."
node rest_api.js &  # Start the REST API server by running the Node.js script (rest_api.js) in the background
API_PID=$!  # Capture the Process ID (PID) of the API server so we can later stop it if needed

# Wait for the API to initialize
sleep 2  # Wait for 2 seconds to give the API time to initialize before proceeding with the tests

# 4. Run the tests
echo "Running tests..."
robot test_rest_api.robot  # Run the Robot Framework tests using the 'robot' command, targeting the test file 'test_rest_api.robot'

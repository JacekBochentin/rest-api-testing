#!/bin/bash

# Skrypt do automatycznej instalacji i uruchomienia projektu

# 1. Instalacja zależności Node.js
echo "Installing Node.js dependencies..."
npm install express

# 2. Instalacja zależności Python
echo "Installing Python dependencies..."
pip install robotframework requests

# 3. Uruchomienie REST API w tle
echo "Starting REST API..."
node rest_api.js &
API_PID=$! # Zapisz PID procesu API

# Poczekaj, aż API się uruchomi
sleep 2

# 4. Uruchomienie testów
echo "Running tests..."
robot test_rest_api.robot
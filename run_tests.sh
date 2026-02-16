#!/bin/bash

# 1. LOCATE 
VENV_PATH="./venv/Scripts/activate"

# 2. ACTIVATE VIRUTAL ENV
# USE 'source' TO RUN SCRIPT
if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
else
    echo "Error: Virtual environment gak ketemu di $VENV_PATH"
    exit 1
fi

# 3. Running TEst Suite
# Call pytest to run  test app
python -m pytest test_app.py

# 4. HANDLE EXIT CODES
# $? save last status
if [ $? -eq 0 ]; then
    echo "Mantap! Semua test lolos."
    exit 0 # goal
else
    echo "Aduh! Ada test yang gagal nih."
    exit 1 # fail
fi
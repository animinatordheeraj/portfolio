#!/bin/bash

# ==========================================
# Portfolio Website - Setup Script (macOS/Linux)
# ==========================================

echo ""
echo "======================================================"
echo " Portfolio Website Setup"
echo "======================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[✓] Python detected"
echo ""

# Create virtual environment
echo "[1/4] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi
echo "[✓] Virtual environment created"
echo ""

# Activate virtual environment
echo "[2/4] Activating virtual environment..."
source venv/bin/activate
echo "[✓] Virtual environment activated"
echo ""

# Install requirements
echo "[3/4] Installing dependencies..."
pip install -r requirements.txt -q
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "[✓] Dependencies installed"
echo ""

# Ready to run
echo "[4/4] Setup complete!"
echo ""
echo "======================================================"
echo " TO START THE SERVER:"
echo "======================================================"
echo ""
echo "1. Make sure you're in the project directory"
echo "2. Run: python app.py"
echo "3. Open your browser to: http://localhost:5000"
echo ""
echo "======================================================"
echo " TEST CREDENTIALS:"
echo "======================================================"
echo ""
echo "Email: test@example.com"
echo "Password: password123 (register first)"
echo ""
echo "======================================================"
echo ""

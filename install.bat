@echo off
REM Installation script for Formly Backend (Windows)

echo 🚀 Formly Backend Installation Script
echo ==================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo ✅ Python is available

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ✅ Installation complete!
echo.
echo To start the application:
echo 1. Activate virtual environment: venv\Scripts\activate.bat
echo 2. Run the application: python -m uvicorn app.main:app --reload
echo.
echo For development:
echo pip install -r requirements-dev.txt

pause

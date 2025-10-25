@echo off
REM Formly Backend - Quick Run Script

echo 🚀 Starting Formly Backend...
echo ============================

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found. Please run install.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Run the application
echo 🚀 Starting development server...
echo Server will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

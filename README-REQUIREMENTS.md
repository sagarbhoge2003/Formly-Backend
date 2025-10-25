# 📦 Requirements Management

This document explains the requirements files and setup for the Formly Backend project.

## 📋 Requirements Files Overview

| File | Purpose | Use Case |
|------|---------|----------|
| `requirements.txt` | **Main requirements** | Core dependencies for running the application |
| `requirements-prod.txt` | **Production requirements** | Minimal dependencies for production deployment |
| `requirements-dev.txt` | **Development requirements** | All dependencies + development tools |

## 🚀 Quick Start

### Option 1: Automated Installation (Recommended)
```bash
# Windows
install.bat

# Linux/Mac
chmod +x install.sh
./install.sh
```

### Option 2: Manual Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt
```

## 📊 Dependencies Breakdown

### Core Application Dependencies
- **FastAPI** (0.104.1) - Modern web framework
- **Uvicorn** (0.24.0) - ASGI server
- **AsyncPG** (0.29.0) - PostgreSQL async driver
- **Pydantic** (2.5.0) - Data validation
- **Pydantic-Settings** (2.1.0) - Settings management

### Security & Authentication
- **Passlib** (1.7.4) - Password hashing with bcrypt
- **Python-JOSE** (3.3.0) - JWT token handling
- **Email-Validator** (2.1.0) - Email validation

### Development Tools (requirements-dev.txt only)
- **Pytest** (7.4.3) - Testing framework
- **Pytest-Asyncio** (0.21.1) - Async testing support
- **Black** (23.11.0) - Code formatter
- **Isort** (5.12.0) - Import sorter
- **Flake8** (6.1.0) - Linter
- **MyPy** (1.7.1) - Type checker

## 🔧 Available Scripts

### Windows
- `install.bat` - Automated installation
- `run.bat` - Quick start development server

### Cross-Platform (Makefile)
```bash
make help          # Show available commands
make install       # Install production dependencies
make install-dev   # Install development dependencies
make run           # Run development server
make test          # Run tests
make lint          # Run linting
make format        # Format code
make clean         # Clean temporary files
```

## 🏗️ Project Structure

```
Formly-Backend/
├── requirements.txt          # Main requirements
├── requirements-prod.txt     # Production requirements
├── requirements-dev.txt      # Development requirements
├── install.bat              # Windows installation script
├── install.sh               # Linux/Mac installation script
├── run.bat                  # Windows quick start
├── makefile                 # Cross-platform commands
└── README-REQUIREMENTS.md   # This file
```

## 🚀 Running the Application

### Development Mode
```bash
# Using batch file (Windows)
run.bat

# Using make
make run

# Manual
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
# Using make
make run-prod

# Manual
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🧪 Testing

```bash
# Run tests
make test

# Run tests with coverage
make test-cov

# Manual
pytest
pytest --cov=app
```

## 🎨 Code Quality

```bash
# Format code
make format

# Run linting
make lint

# Manual
black app/
isort app/
flake8 app/
mypy app/
```

## 🔍 Troubleshooting

### Common Issues

1. **Virtual Environment Not Found**
   ```bash
   python -m venv venv
   ```

2. **Permission Denied (Linux/Mac)**
   ```bash
   chmod +x install.sh
   chmod +x run.sh
   ```

3. **Python Not Found**
   - Install Python 3.8+ from [python.org](https://python.org)

4. **Pip Not Found**
   ```bash
   python -m ensurepip --upgrade
   ```

### Environment Variables

Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/formly_db
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## 📈 Performance Notes

- **Connection Pooling**: The application uses AsyncPG connection pooling for optimal database performance
- **Production**: Use `requirements-prod.txt` for smaller deployment footprint
- **Development**: Use `requirements-dev.txt` for full development experience

## 🔄 Updates

To update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

To add new dependencies:
1. Add to appropriate requirements file
2. Update this documentation
3. Test installation with `pip install --dry-run -r requirements.txt`

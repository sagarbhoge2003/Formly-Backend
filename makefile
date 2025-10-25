# Formly Backend Makefile

.PHONY: help install install-dev install-prod run test lint format clean

help: ## Show this help message
	@echo "Formly Backend - Available Commands:"
	@echo "=================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt

install-prod: ## Install production dependencies only
	pip install -r requirements-prod.txt

run: ## Run the development server
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Run the production server
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=app

lint: ## Run linting
	flake8 app/
	mypy app/

format: ## Format code
	black app/
	isort app/

clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/

setup: install-dev ## Setup development environment
	@echo "✅ Development environment setup complete!"
	@echo "Run 'make run' to start the development server"
.PHONY: help install install-dev test coverage lint format clean docs build upload

# Default target
help:
	@echo "pyhmong - Development Commands"
	@echo "=============================="
	@echo ""
	@echo "Available commands:"
	@echo "  make install       - Install package"
	@echo "  make install-dev   - Install package with dev dependencies"
	@echo "  make test          - Run tests"
	@echo "  make coverage      - Run tests with coverage report"
	@echo "  make lint          - Run linting (flake8, mypy)"
	@echo "  make format        - Format code with black and isort"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make docs          - Build documentation"
	@echo "  make build         - Build distribution packages"
	@echo "  make upload        - Upload to PyPI"
	@echo "  make upload-test   - Upload to TestPyPI"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Testing
test:
	pytest

coverage:
	pytest --cov=pyhmong --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

# Code quality
lint:
	@echo "Running flake8..."
	flake8 pyhmong tests
	@echo "Running mypy..."
	mypy pyhmong
	@echo "Running pylint..."
	pylint pyhmong

format:
	@echo "Running black..."
	black pyhmong tests
	@echo "Running isort..."
	isort pyhmong tests

# Cleaning
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.so" -delete
	@echo "Clean complete!"

# Documentation
docs:
	cd docs && make html
	@echo "Documentation built in docs/_build/html/index.html"

# Building and distribution
build: clean
	python -m build

upload: build
	twine upload dist/*

upload-test: build
	twine upload --repository testpypi dist/*

# Development workflow
dev: format lint test
	@echo "Development checks complete!"

# Quick checks before commit
pre-commit: format lint
	@echo "Pre-commit checks complete!"
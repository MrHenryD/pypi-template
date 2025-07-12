.PHONY: help install test test-unit test-integration test-performance test-all clean lint format type-check coverage docs

help:
	@echo "Available commands:"
	@echo "  help          - Show this help message"
	@echo "  setup-pyenv   - Set up Python environment with pyenv and virtualenv"
	@echo "  install        - Install package in development mode"
	@echo "  install-dev    - Install with development dependencies"
	@echo "  test          - Run unit tests (default)"
	@echo "  test-unit     - Run unit tests only"
	@echo "  test-integration - Run integration tests"
	@echo "  test-performance - Run performance tests"
	@echo "  test-all      - Run all tests"
	@echo "  coverage      - Run tests with coverage report"
	@echo "  coverage-html - Run tests with HTML coverage report"
	@echo "  lint          - Run flake8 linting"
	@echo "  format        - Format code with black"
	@echo "  type-check    - Run mypy type checking"
	@echo "  clean         - Clean up temporary files"
	@echo "  ci            - Run all CI checks (lint, type-check, test-all)"


setup-pyenv:
	pyenv local 3.11;
	python3 -m virtualenv venv;

install:
	poetry install

install-dev:
	poetry install --extras dev

test: test-unit

test-unit:
	poetry run pytest -m "unit" tests/ -v

test-integration:
	poetry run pytest -m "integration" tests/ -v

test-performance:
	poetry run pytest -m "performance" tests/ -v

test-all:
	poetry run pytest tests/ -v

coverage:
	poetry run pytest --cov=teenytiny --cov-report=term-missing tests/

coverage-html:
	poetry run pytest --cov=teenytiny --cov-report=html --cov-report=term-missing tests/
	@echo "HTML coverage report generated in htmlcov/"

lint:
	poetry run flake8 teenytiny/

format:
	poetry run black teenytiny/ tests/

type-check:
	poetry run mypy teenytiny/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/

ci: lint type-check test-all
	@echo "All CI checks passed!"

pre-release: lint type-check test-all
	poetry run python utils/version.py $(CHANGE_TYPE)

build-release:
	poetry build

release-pypi-test:
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry config pypi-token.testpypi $(PYPI_TOKEN_TEST)
	poetry publish --build --repository testpypi

.PHONY: help setup install lock format lint test clean run

# Default target - show help
help:
	@echo "Available commands:"
	@echo "  make setup    - Install dependencies using uv sync"
	@echo "  make install  - Alias for setup"
	@echo "  make lock     - Create/update uv.lock file"
	@echo "  make format   - Format code using ruff"
	@echo "  make lint     - Lint code using ruff"
	@echo "  make test     - Run tests with pytest"
	@echo "  make clean    - Remove build artifacts and caches"
	@echo "  make run      - Run the application"

# === Development Setup ===

# Install dependencies using uv sync
setup:
	uv sync

# Alias for setup
install: setup

# Create/update uv.lock file
lock:
	uv lock

# === Code Quality ===

# Format code using ruff
format:
	ruff format --line-length 100 .

# Lint code using ruff
lint:
	ruff check --line-length 100 .

# === Testing ===

# Run tests
test:
	pytest

# === Application ===

# Run the application
run:
	uv run python -m clear_plex_watchlist

# === Cleanup ===

# Clean build artifacts and cache
clean:
	rm -rf .ruff_cache
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf build
	rm -rf .uv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
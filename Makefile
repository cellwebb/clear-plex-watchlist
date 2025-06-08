.PHONY: setup format lint test clean sync lock run

# Setup development environment
setup:
	uv sync

# Format code using ruff
format:
	ruff format --line-length 100 .

# Lint code using ruff
lint:
	ruff check --line-length 100 .

# Run tests
test:
	pytest

# Clean build artifacts and cache
clean:
	rm -rf .ruff_cache
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf build
	rm -rf .uv

# Install dependencies using uv sync
install:
	uv sync

# Create/update uv.lock file
lock:
	uv lock

# Run the application
run:
	uv run python -m clear_plex_watchlist

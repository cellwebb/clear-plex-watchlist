# clear-plex-watchlist

A utility to clear Plex watchlists efficiently.

## Installation

```bash
uv sync
```

The project uses a `uv.lock` file to ensure reproducible dependency installations across environments.

## Usage

```bash
python -m clear_plex_watchlist
```

## Development

This project uses:

- `uv` for package management with lockfile support (`uv.lock`)
- `ruff` for code formatting and linting with 100 character line limit
- `pytest` for testing

### Makefile Commands

```bash
# Setup development environment
make setup

# Format code
make format

# Lint code
make lint

# Run tests
make test

# Clean build artifacts
make clean

# Create or update uv.lock file
make lock

# Install dependencies using uv sync
make install

# Install dev dependencies using uv sync
make install-dev
```

# clear-plex-watchlist

A utility to clear Plex watchlists efficiently.

## Requirements

- Python 3.12 or higher
- Plex account credentials

## Installation

### From source

```bash
git clone https://github.com/cellwebb/clear-plex-watchlist.git
cd clear-plex-watchlist
uv sync
```

The project uses a `uv.lock` file to ensure reproducible dependency installations across environments.

## Configuration

Set the following environment variables:

```bash
export PLEX_USERNAME="your_plex_username"
export PLEX_PASSWORD="your_plex_password"
```

## Usage

The utility can be run in several ways:

```bash
# Using the installed command (after installation)
clear-plex-watchlist

# As a Python module
python -m clear_plex_watchlist

# Direct script execution
python clear-plex-watchlist.py
```

The script will:
1. Authenticate with your Plex account
2. Connect to your first available Plex server
3. Fetch all items in your watchlist
4. Remove each item one by one
5. Report progress and any errors encountered

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

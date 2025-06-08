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

### Environment Variables

You can configure the application using environment variables in two ways:

#### Option 1: Environment Variables
```bash
export PLEX_USERNAME="your_plex_username"
export PLEX_PASSWORD="your_plex_password"
```

#### Option 2: .env File (Recommended)
Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env

# Edit with your credentials
PLEX_USERNAME=your_plex_username
PLEX_PASSWORD=your_plex_password
```

The application will automatically load variables from the `.env` file if present.

## Usage

The utility can be run in several ways:

```bash
# Using make (recommended)
make run

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

Run `make help` to see all available commands:

```bash
# Show help
make help

# Development setup
make setup    # Install dependencies using uv sync
make install  # Alias for setup
make lock     # Create/update uv.lock file

# Code quality
make format   # Format code using ruff
make lint     # Lint code using ruff

# Testing
make test     # Run tests with pytest

# Application
make run      # Run the application

# Cleanup
make clean    # Remove build artifacts and caches
```

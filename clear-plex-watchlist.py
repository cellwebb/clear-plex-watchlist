
import os
import logging
from typing import List, Optional

from plexapi.myplex import MyPlexAccount
from plexapi.exceptions import BadRequest, NotFound
from plexapi.video import Video


def get_plex_credentials() -> tuple[str, str]:
    """Retrieve and validate Plex credentials from environment variables."""
    username = os.getenv('PLEX_USERNAME')
    password = os.getenv('PLEX_PASSWORD')
    
    if not username or not password:
        raise ValueError("Set PLEX_USERNAME and PLEX_PASSWORD environment variables")
    
    return username, password


def remove_watchlist_item(item: Video) -> bool:
    """Remove a single item from the watchlist and return success status."""
    try:
        item.removeFromWatchlist()
        logging.info(f"Removed: {item.title}")
        return True
    except (BadRequest, NotFound) as e:
        logging.error(f"Failed to remove {item.title}: {e}")
        return False


def clear_plex_watchlist() -> None:
    """Clear all items from Plex watchlist."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    
    try:
        username, password = get_plex_credentials()
        account = MyPlexAccount(username, password)
        logging.info(f"Connected to Plex account: {account.username}")
        
        watchlist = account.watchlist()
        
        if not watchlist:
            logging.info("Watchlist is already empty")
            return
        
        logging.info(f"Found {len(watchlist)} items in watchlist")
        
        success_count = sum(remove_watchlist_item(item) for item in watchlist)
        logging.info(f"Removed {success_count} of {len(watchlist)} items successfully")
        
    except Exception as e:
        logging.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    clear_plex_watchlist()


import os
from plexapi.myplex import MyPlexAccount
from plexapi.exceptions import BadRequest, NotFound


def clear_plex_watchlist():
    """Clear all items from Plex watchlist."""
    
    # Get credentials from environment variables
    username = os.getenv('PLEX_USERNAME')
    password = os.getenv('PLEX_PASSWORD')
    
    if not username or not password:
        raise ValueError("Set PLEX_USERNAME and PLEX_PASSWORD environment variables")
    
    try:
        # Connect to Plex account
        account = MyPlexAccount(username, password)
        print(f"Connected to Plex account: {account.username}")
        
        # Get watchlist
        watchlist = account.watchlist()
        
        if not watchlist:
            print("Watchlist is already empty")
            return
        
        print(f"Found {len(watchlist)} items in watchlist")
        
        # Remove each item
        for item in watchlist:
            try:
                item.removeFromWatchlist()
                print(f"Removed: {item.title}")
            except (BadRequest, NotFound) as e:
                print(f"Failed to remove {item.title}: {e}")
        
        print("Watchlist cleared successfully")
        
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    clear_plex_watchlist()

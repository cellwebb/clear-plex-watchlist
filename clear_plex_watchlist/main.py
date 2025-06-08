import logging
import os
import time
from socket import error as SocketError
from typing import Tuple

from dotenv import load_dotenv
from plexapi.exceptions import BadRequest, NotFound
from plexapi.myplex import MyPlexAccount
from plexapi.video import Video


def get_plex_credentials() -> Tuple[str, str]:
    """Retrieve and validate Plex credentials from environment variables."""
    username = os.getenv("PLEX_USERNAME")
    password = os.getenv("PLEX_PASSWORD")

    if not username or not password:
        raise ValueError("Set PLEX_USERNAME and PLEX_PASSWORD environment variables")

    return username, password


def remove_watchlist_item(item: Video, account: MyPlexAccount, retry_count: int = 3, retry_delay: float = 1.0) -> bool:
    """Remove a single item from the watchlist with retry logic and return success status."""
    for attempt in range(retry_count):
        try:
            # Pass the account parameter to removeFromWatchlist
            item.removeFromWatchlist(account=account)
            logging.info(f"Removed: {item.title}")
            return True
        except SocketError as e:
            if e.errno == 104:  # Connection reset by peer
                if attempt < retry_count - 1:
                    wait_time = retry_delay * (2 ** attempt)  # Exponential backoff
                    logging.warning(f"Connection reset for {item.title}, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    logging.error(f"Failed to remove {item.title} after {retry_count} attempts: Connection reset")
                    return False
            else:
                logging.error(f"Socket error removing {item.title}: {e}")
                return False
        except (BadRequest, NotFound) as e:
            logging.error(f"Failed to remove {item.title}: {e}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error removing {item.title}: {e}")
            return False
    
    return False


def clear_plex_watchlist(batch_size: int = 10, batch_delay: float = 1.0) -> None:
    """Clear all items from Plex watchlist with batch processing to avoid rate limiting.
    
    Args:
        batch_size: Number of items to process before adding a delay
        batch_delay: Seconds to wait between batches
    """
    load_dotenv()
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
        logging.info(f"Processing in batches of {batch_size} items with {batch_delay}s delay between batches")

        success_count = 0
        for i, item in enumerate(watchlist):
            # Pass the account parameter to the remove function
            if remove_watchlist_item(item, account):
                success_count += 1
            
            # Add delay after each batch to avoid rate limiting
            if (i + 1) % batch_size == 0 and i < len(watchlist) - 1:
                logging.info(f"Processed {i + 1}/{len(watchlist)} items, pausing for {batch_delay}s...")
                time.sleep(batch_delay)

        logging.info(f"Removed {success_count} of {len(watchlist)} items successfully")

    except Exception as e:
        logging.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    clear_plex_watchlist()

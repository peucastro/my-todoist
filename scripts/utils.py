import os
import logging
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI


def setup_logging():
    """Configure logging based on LOG_LEVEL environment variable."""
    load_dotenv()
    log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.WARNING),
        format="%(levelname)s: %(message)s",
    )


def get_api_client() -> TodoistAPI:
    """Load API token from environment and return configured TodoistAPI client."""
    load_dotenv()
    api_token = os.getenv("TODOIST_API_TOKEN")
    if not api_token:
        logging.error("TODOIST_API_TOKEN not found in .env file.")
        raise ValueError("TODOIST_API_TOKEN is required")
    return TodoistAPI(api_token)

import os
import logging
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
from scripts.delete_completed_tasks import delete_completed_tasks


def main():
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

    if not load_dotenv():
        logging.warning("No environment variable is set.")
        return

    api_token = os.getenv("TODOIST_API_TOKEN")
    if not api_token:
        logging.error("TODOIST_API_TOKEN not found in .env file.")
        return

    api = TodoistAPI(api_token)
    delete_completed_tasks(api)


if __name__ == "__main__":
    main()

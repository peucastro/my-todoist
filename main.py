import os
import logging
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI


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
    try:
        projects = api.get_projects()
        print(f"Found {len(projects)} projects:")
        for project in projects:
            print(f"- {project.name}")
    except Exception as e:
        logging.error(f"API test failed: {e}")


if __name__ == "__main__":
    main()

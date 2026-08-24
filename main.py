from scripts.delete_completed_tasks import delete_completed_tasks
from scripts.utils import get_api_client, setup_logging


def main():
    setup_logging()

    try:
        api = get_api_client()
    except ValueError:
        return

    delete_completed_tasks(api)


if __name__ == "__main__":
    main()

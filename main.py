from scripts.utils import setup_logging, get_api_client
from scripts.delete_completed_tasks import delete_completed_tasks


def main():
    setup_logging()

    try:
        api = get_api_client()
    except ValueError:
        return

    delete_completed_tasks(api)


if __name__ == "__main__":
    main()

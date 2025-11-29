import logging
from todoist_api_python.api import TodoistAPI


def delete_completed_tasks(api: TodoistAPI):
    """Delete all completed tasks."""
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

    try:
        logging.info("Fetching all projects...")
        deleted_count = 0

        projects = api.get_projects()
        for project in projects:
            logging.info(f"Checking project: {project.name}")
            tasks = api.get_tasks(project_id=project.id)
            for task in tasks:
                if task.is_completed:
                    try:
                        api.delete_task(task.id)
                        logging.info(f"Deleted task: {task.content}")
                        deleted_count += 1
                    except Exception as e:
                        logging.error(f"Failed to delete task {task.id}: {e}")

        if deleted_count == 0:
            logging.info("No completed tasks found.")
        else:
            logging.info(f"Successfully delete {deleted_count} completed tasks.")

    except Exception as e:
        logging.error(f"API error: {e}")

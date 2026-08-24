import logging

from todoist_api_python.api import TodoistAPI

logger = logging.getLogger(__name__)


def delete_completed_tasks(api: TodoistAPI):
    """Delete all completed tasks."""
    try:
        logger.info("Fetching all projects...")
        deleted_count = 0

        projects = api.get_projects()
        for project in projects:
            logger.info(f"Checking project: {project.name}")
            tasks = api.get_tasks(project_id=project.id)
            for task in tasks:
                if task.is_completed:
                    try:
                        api.delete_task(task.id)
                        logger.info(f"Deleted task: {task.content}")
                        deleted_count += 1
                    except Exception as e:  # noqa: BLE001
                        logger.error(f"Failed to delete task {task.id}: {e}")

        if deleted_count == 0:
            logger.info("No completed tasks found.")
        else:
            logger.info(f"Successfully delete {deleted_count} completed tasks.")

    except Exception as e:  # noqa: BLE001
        logger.error(f"API error: {e}")

import json
from typing import Callable
from ..utils import FileManager


def update_task(
    database: list,
    file_manager: FileManager,
    task_id: str,
    updated_task: str,
):
    updated_tasks = []

    for task in database:
        if task.get("id") == task_id:
            parsed_updated_task = json.loads(updated_task)
            parsed_updated_task["id"] = task["id"]
            updated_tasks.append(parsed_updated_task)
        else:
            updated_tasks.append(task)

    file_manager.write(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

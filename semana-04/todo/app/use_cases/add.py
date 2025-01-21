import uuid
import json
from ..utils import FileManager


def validate_task_struct(task: dict):
    keys = task.keys()
    required_keys = ["status", "desc"]
    diff: set = required_keys - keys

    if len(diff) > 0:
        print(f"Error: {required_keys} are required in data struct")
        return True

    if task.get("status") not in ["in progress", "done", "not done"]:
        print(f"Error: status must be 'in progress' or 'done'")
        return True

    if task.get("desc") is None or len(task.get("desc")) == 0:
        print(f"Error: desc should not be empty")
        return True

    return False


def generate_task_id(task: dict):
    task["id"] = str(uuid.uuid1()).split("-")[0]
    return task


def add_task(
    database: list,
    file_manager: FileManager,
    new_task: str,
):
    task_parsed = json.loads(new_task)

    has_error = validate_task_struct(task_parsed)
    if has_error:
        return

    task_with_id = generate_task_id(task_parsed)
    database.append(task_with_id)
    file_manager.write(database)

    print(file_manager.read())
    print("Task added successfully!")

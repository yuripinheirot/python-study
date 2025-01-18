import json
from file_manager import read_file,write_file
from decorators import custom_logger

tasks: list = read_file.execute()

@custom_logger.execute
def update_task(task_id: str, data: str):
    updated_tasks = []

    for task in tasks:
        if task.get("id") == task_id:
            parsed_updated_task = json.loads(data)
            parsed_updated_task["id"] = task["id"]
            updated_tasks.append(parsed_updated_task)
        else:
            updated_tasks.append(task)

    write_file.execute(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

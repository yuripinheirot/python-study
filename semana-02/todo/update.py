import json
from file_manager import read_file,write_file

tasks: list = read_file()

def update_task(task_id: str, data: str):
    updated_tasks = []

    for task in tasks:
        if task["id"] == task_id:
            parsed_updated_task = json.loads(data)
            parsed_updated_task["id"] = task["id"]
            updated_tasks.append(parsed_updated_task)
        else:
            updated_tasks.append(task)

    write_file(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

import json
from file_manager import read_file,write_file

tasks: list = read_file()

def delete_task(task_id: str):
    updated_tasks = []

    for task in tasks:
        if task["id"] != task_id:
            updated_tasks.append(task)

    if len(tasks) == len(updated_tasks):
        return print("Task to delete not found!")

    write_file(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

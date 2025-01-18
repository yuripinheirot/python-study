from file_manager import read_file, write_file
from decorators import custom_logger

tasks: list = read_file.execute()

@custom_logger.execute
def delete_task(task_id: str):
    updated_tasks = [task for task in tasks if task.get("id") != task_id ]

    if len(tasks) == len(updated_tasks):
        return print("Task to delete not found!")

    write_file.execute(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

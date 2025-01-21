from ..utils import FileManager


def delete_task(database: list, file_manager: FileManager, task_id: str):
    updated_tasks = [task for task in database if task.get("id") != task_id]

    if len(database) == len(updated_tasks):
        return print("Task to delete not found!")

    file_manager.write(updated_tasks)
    print(updated_tasks)
    print("Task deleted successfully!")

from file_manager import read_file
from decorators import custom_logger

tasks: list = read_file.execute()


def filter_tasks(status):
    status_dict = {
        "list-done": "done",
        "list-in-progress": "in progress",
        "list-not-done": "not done",
        "list-all": None
    }
    if status == "list-all":
        return tasks

    tasks_filtered = [t for t in tasks if t.get("status") == status_dict[status]]

    return tasks_filtered

@custom_logger.execute
def list_tasks(action: str):
    filtered_tasks = filter_tasks(action)
    print(filtered_tasks)
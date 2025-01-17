from file_manager import read_file

tasks: list = read_file()

def filter_tasks(status):
    status_dict = {
        "list-done": "done",
        "list-in-progress": "in progress",
        "list-not-done": "not done",
    }

    tasks_filtered = []

    for task in tasks:
        if task.get("status") == status_dict[status]:
            tasks_filtered.append(task)

    return tasks_filtered

def list_tasks(action: str):
    filtered_tasks = filter_tasks(action)
    print(filtered_tasks)
from file_manager import read_file

tasks: list = read_file.execute()

def filter_tasks(status):
    status_dict = {
        "list-done": "done",
        "list-in-progress": "in progress",
        "list-not-done": "not done",
    }

    tasks_filtered = [t for t in tasks if t.get("status") == status_dict[status]]

    return tasks_filtered

def list_tasks(action: str):
    filtered_tasks = filter_tasks(action)
    print(filtered_tasks)
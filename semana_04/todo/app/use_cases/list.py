def filter_tasks(
    database: list,
    status: str,
):
    status_dict = {
        "list-done": "done",
        "list-in-progress": "in progress",
        "list-not-done": "not done",
        "list-all": None,
    }
    if status == "list-all":
        return database

    tasks_filtered = [t for t in database if t.get("status") == status_dict[status]]

    return tasks_filtered


def list_tasks(
    database: list,
    action: str,
):
    filtered_tasks = filter_tasks(
        database,
        action,
    )
    print(filtered_tasks)

import json
import uuid

from file_manager import write_file, read_file

def validate_task_struct(task: dict):
    keys = task.keys()
    required_keys = ["status", "desc"]
    diff: set = required_keys - keys

    if len(diff) > 0:
        print(f"Error: {list(required_keys)} are required in data struct")
        return True

    if task["status"] not in ["in progress", "done", "not done"]:
        print(f"Error: status must be 'in progress' or 'done'")
        return True

    if len(task["desc"]) == 0:
        print(f"Error: desc should not be empty")
        return True

    return False

def generate_task_id(task: dict):
    task["id"] = uuid.uuid1().__str__().split('-')[0]
    return task



def add_task(data: json, task):
    task_parsed = json.loads(task)

    has_error = validate_task_struct(task_parsed)
    if has_error:
        return

    task_with_id = generate_task_id(task_parsed)
    data.append(task_with_id)
    write_file(data)

    print(read_file())
    print("Task added successfully!")
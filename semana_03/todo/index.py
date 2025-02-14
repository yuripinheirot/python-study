from custom_cli import read_args
from file_manager import read_file

from list import list_tasks
from add import add_task
from update import update_task
from delete import delete_task


args = read_args.execute()
data = read_file.execute()


def execute():
    if args.action in ['list-done','list-in-progress','list-done','list-not-done', 'list-all']:
        return list_tasks(args.action)
    if args.action == 'add':
        if args.data is None:
            return print("Error: argument '--data' is required")
        return add_task(data, args.data)
    if args.action == 'update':
        if args.id is None:
            return print("Error: argument '--id' is required")
        if args.data is None:
            return print("Error: argument '--data' is required")
        update_task(args.id, args.data)
    if args.action == 'delete':
        if args.id is None:
            return print("Error: argument '--id' is required")
        delete_task(args.id)



execute()
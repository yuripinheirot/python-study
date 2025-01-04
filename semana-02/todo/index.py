from mycli import read_args
from file_manager import read_file
from add import add_task
from list import list_tasks
from update import update_task
from delete import  delete_task


args = read_args()
data = read_file()


def execute():
    if args.action == 'list-all':
        return print(data)
    if args.action in ['list-done','list-in-progress','list-done','list-not-done']:
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
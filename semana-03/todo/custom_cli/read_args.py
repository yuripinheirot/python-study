import argparse

action_opts = ("list-all","list-done","list-not-done","list-in-progress", "add", "update", "delete", "set-in-progress", "set-done")

def execute():
    parser = argparse.ArgumentParser(description='To-Do List')

    parser.add_argument('--action', choices=action_opts, type=str, help='Action to execute')
    parser.add_argument('--id', type=str, help='Identifier task')
    parser.add_argument('--data', type=str, help='Data task to write')

    args = parser.parse_args()

    return args 


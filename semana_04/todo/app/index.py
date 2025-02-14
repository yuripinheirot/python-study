import os
from typing import Callable, TypedDict

from .utils.file_manager import FileManager
from .use_cases import add_task, update_task, delete_task, list_tasks


class ParamTypes(TypedDict):
    data: str


class App:
    def __init__(self):
        database_path = os.path.join(os.getcwd(), "app", "data", "data.json")

        self.file_manager = FileManager(database_path)
        self.database = self.file_manager.read()

        self.actions = {
            "add": {"method": add_task},
            "update": {"method": update_task},
            "delete": {"method": delete_task},
            "list": {"method": list_tasks},
        }

    def add(self, data: str):
        return add_task(
            self.database,
            self.file_manager,
            data,
        )

    def update(
        self,
        data: str,
        id: str,
    ):
        return update_task(
            self.database,
            self.file_manager,
            id,
            data,
        )

    def list(self, data, id, action: str):
        return list_tasks(self.database, action)

    def delete(self, data, id: str):
        return delete_task(self.database, self.file_manager, id)

    def execute(self, data, id: str, action: str):
        action_parsed = action.split("-")[0]
        method: Callable = self.actions.get(action_parsed).get("method")
        return method(data, id, action)

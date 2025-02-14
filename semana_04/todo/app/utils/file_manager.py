import json


class FileManager:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def read(self):
        with open(self.json_path, "r") as file:
            data = file.read()
            return json.loads(data)

    def write(self, data: list):
        with open(self.json_path, "w") as file:
            file.write(json.dumps(data))
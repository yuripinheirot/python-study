import json

def execute():
    with open("data.json", "r") as file:
        data = file.read()
        return json.loads(data)
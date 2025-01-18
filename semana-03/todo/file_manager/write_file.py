import json

def execute(data: dict):
    with open("data.json", "w") as file:
        file.write(json.dumps(data))
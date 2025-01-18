import json

def execute(data: list):
    with open("data.json", "w") as file:
        file.write(json.dumps(data))
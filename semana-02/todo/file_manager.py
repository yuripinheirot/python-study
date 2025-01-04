import json

def read_file():
    with open("data.json", "r") as file:
        data = file.read()
        return json.loads(data)

def write_file(data):
    with open("data.json", "w") as file:
        file.write(json.dumps(data))
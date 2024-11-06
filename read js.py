import json
# Reading from the JSON file
with open("data.json", "r") as file:
    data = json.load(file)
print("Content of data.json:")
print(data)
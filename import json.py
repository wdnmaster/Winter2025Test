import json

# Data to store in the JSON file
data = {
    "name": "Welid",
    "age": 24,
    "class": "IT115"
}

# Creating a JSON file
with open("welid_info.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file 'welid_info.json' has been created successfully!")

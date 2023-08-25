import json

data_dict = {
    1: ['s', 't', 'u', 'v', 'w', 'x'],
    2: ['a', 'b', 'c', 'd', 'e', 'f']
}

json_file_path = 'data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Словарь успешно записан в JSON файл.")

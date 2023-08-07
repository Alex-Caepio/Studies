import json

data_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 28
}

json_file_path = 'data_file.json'

with open(json_file_path, 'w') as json_file:
    for name, age in data_dict.items():
        entry = {"name": name, "age": age}
        json.dump(entry, json_file)
        json_file.write('\n')

print("Данные успешно записаны в JSON файл построчно.")

json_file_path = 'data_file.json'
new_data_dict = {}

with open(json_file_path, 'r') as json_file:
    for line in json_file:
        entry = json.loads(line)
        new_data_dict[entry['name']] = entry['age']

print(new_data_dict)

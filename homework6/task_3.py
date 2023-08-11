import json

data_dict = {
    123456: ("Alice", 25),
    234567: ("Bob", 30),
    345678: ("Charlie", 28),
    456789: ("David", 22),
    567890: ("Eva", 27),
    678901: ("Frank", 32)
}

json_file_path = 'data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Словарь успешно записан в JSON файл.")

import json
import csv

json_file_path = 'data.json'

phone_dict = {
    "Alice": "123456789",
    "Bob": "234567890",
    "Charlie": "345678901",
    "David": "456789012",
    "Eva": "567890123",
    "Frank": "678901234"
}

with open(json_file_path, 'r') as json_file:
    data_dict = json.load(json_file)

csv_file_path = 'data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['ID', 'Имя', 'Возраст', 'Телефон']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for id_num, (name, age) in data_dict.items():
        phone = phone_dict.get(name, "")
        writer.writerow({'ID': id_num, 'Имя': name, 'Возраст': age, 'Телефон': phone})

print("Данные успешно записаны в CSV файл.")

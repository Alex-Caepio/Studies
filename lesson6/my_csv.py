import csv

with open('data.csv', 'w') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    writer.writerow({'name': 'Bob', 'age': 25, 'job': 'Dev'})
    writer.writerow({'name': 'Alice', 'age': 28, 'job': 'Dev'})
    writer.writerow({'name': 'Charlie', 'age': 30, 'job': 'Manager'})

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        print(row['name'], row['age'], row['job'])

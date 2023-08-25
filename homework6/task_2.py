line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")

file_path = 'output_file.txt'
with open(file_path, 'w') as file:
    file.write(line1 + '\n')
    file.write(line2 + '\n')

print("Первые 2 строки успешно записаны в файл.")

line3 = input("Введите третью строку: ")
line4 = input("Введите четвертую строку: ")

with open(file_path, 'a') as file:
    file.write(line3 + '\n')
    file.write(line4 + '\n')

print("Оставшиеся 2 строки успешно добавлены в файл.")

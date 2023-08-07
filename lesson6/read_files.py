import json

with open('Hello', 'r') as f:
    printlines = f.read()
    print(printlines)
    # for item in printlines:
    #     item.strip('\n')
    #     print(item, end='')

# data_to_write = {
#     "name": "Alex",
#     "age": 35,
#     "isMarried": False,
#     "friends": [
#         {
#             "name": "Bob",
#             "age": 25,
#             "isMarried": False
#         },
#         {
#             "name": "John",
#             "age": 25,
#             "isMarried": False
#         }
#     ]
# }
#
# with open('read_files.py', 'w') as f:
#     json.dump(data_to_write, f)


source_file_path = 'Hello'
new_file_path = 'new.csv'

with open(source_file_path, 'r') as source_file:
    content = source_file.read()

with open(new_file_path, 'w') as new_file:
    new_file.write(content)

print("Файл успешно прочитан и записан с новым форматом.")

with(open('Hello', 'a')) as f:
    for i in range(10):
        f.write('Hello\n')

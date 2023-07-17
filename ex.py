my_list = list(range(1, 13))
squared_list = []

for x in my_list:
    if x % 2 != 0:
        continue
    if x % 10 == 0:
        break
    squared_list.append(x ** 2)

print(squared_list)

print("\n\n'-------'\n")

my_list = list(range(1, 13))
for index, value in enumerate(my_list):
    if value % 2 == 0:
        my_list[index] = "четные"
print(my_list)

rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}

empty_set = set()
print(type(empty_set))

number_list = [1, 43, 56, 3, 3, 3, 3]
text_tuple = ('hello', 'bye', 'hey!', 'hey!', 'hey!')

set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('Yes!!!')
set_from_list.remove(3)
set_from_list.discard(43)  # не возвращает ошибку при удалении несуществующего элемента

print(set_from_list)
print(set_from_tuple)

my_list = [1, 2, 3, 5, 4, 6, 7, 8, 9]

print(len(my_list))

for i in range(len(my_list)):
    print(my_list[i])


# Напиши сортировку пузырьком

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        for j in range(n - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


print(bubble_sort(my_list))

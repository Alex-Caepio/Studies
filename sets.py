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

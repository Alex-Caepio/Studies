my_list = [10, 6, 2, 3]


def sort_by_increase(my_list):
    if len(my_list) == 1:
        return my_list
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return sort_by_increase(my_list[:-1]) + [my_list[-1]]


print(sort_by_increase(my_list))


def bubble_sort_recursive(my_list, n=None):
    if n == None:
        n = len(my_list)

    if n == 1:
        return my_list

    for i in range(n - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return bubble_sort_recursive(my_list, n - 1)


my_list = [10, 6, 2, 3]
sorted_list = bubble_sort_recursive(my_list)
print(sorted_list)

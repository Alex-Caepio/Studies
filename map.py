def sum_of_two_numbers(x):
    return x + x


number_list = [number for number in range(1, 8)]

for item in map(sum_of_two_numbers, number_list):
    print(item)

print(list(map(sum_of_two_numbers, number_list)))


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has no "a"')
        return False


string_list = ['hi', 'was', 'name', 'he']

print(list(map(is_a_in_string, string_list)))

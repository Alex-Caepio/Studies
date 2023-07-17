def is_number_odd(number):
    return number % 2 > 0


number_list = [number for number in range(1, 8)]

print(list(filter(is_number_odd, number_list)))

for number in filter(is_number_odd, number_list):
    print(number)


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has no "a"')
        return False


string_list = ['hi', 'was', 'name', 'he']

print(list(filter(is_a_in_string, string_list)))

help(list)

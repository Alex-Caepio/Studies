number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)

number_list = [6, 43, -2, 11, 0, -55, -12, 3, 345]
number_dict_1 = {number: number ** 2 for number in number_list}
print(number_dict_1)

number_dict_1 = {number: 'positive' if number > 0 else 'negative'
if number < 0 else 'zero' for number in number_list}
print(number_dict_1)

# Set Comprehension

number_list = [6, 43, -2, 11, 0, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list}
print(number_set)

number_list = [6, 43, -2, 11, 0, -55, -12, 3, 345]
number_set = {number ** 2 for number in range(3, 11)}
print(number_set)

letter_set = {letter.upper() for letter in 'Hello'}
print(letter_set)

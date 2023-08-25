def analyze_and_convert(input_string):
    if input_string.lstrip('-').replace('.', '', 1).isdigit():
        if '.' in input_string:
            converted_number = float(input_string)
            if input_string.startswith('-'):
                return f"Вы ввели отрицательное дробное число: {converted_number}"
            else:
                return f"Вы ввели положительное дробное число: {converted_number}"
        else:
            converted_number = int(input_string)
            if input_string.startswith('-'):
                return f"Вы ввели отрицательное целое число: {converted_number}"
            else:
                return f"Вы ввели положительное целое число: {converted_number}"
    else:
        return f"Вы ввели некорректное число: {input_string}"


print(analyze_and_convert("-6.7"))
print(analyze_and_convert("5"))
print(analyze_and_convert("5.4r"))
print(analyze_and_convert("-.777"))

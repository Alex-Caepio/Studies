def validate_input(func):
    def wrapper(input_string):
        if input_string.lstrip('-').replace('.', '', 1).isdigit():
            return func(input_string)
        else:
            return f"Вы ввели некорректное число: {input_string}"

    return wrapper


def is_positive_float(func):
    def wrapper(input_string):
        converted_number = float(input_string)
        if converted_number > 0 and '.' in input_string:
            return func(input_string)
        else:
            return f"Вы ввели отрицательное дробное число: {input_string}"

    return wrapper


def is_negative_float(func):
    def wrapper(input_string):
        converted_number = float(input_string)
        if converted_number < 0 and '.' in input_string:
            return func(input_string)
        else:
            return f"Вы ввели положительное дробное число: {input_string}"

    return wrapper


def is_positive_integer(func):
    def wrapper(input_string):
        if '.' not in input_string:
            converted_number = int(input_string)
            if converted_number > 0:
                return func(input_string)
            else:
                return f"Вы ввели отрицательное целое число: {input_string}"
        else:
            return f"Вы ввели дробное число: {input_string}"

    return wrapper


def is_negative_integer(func):
    def wrapper(input_string):
        if '.' not in input_string:
            converted_number = int(input_string)
            if converted_number < 0:
                return func(input_string)
            else:
                return f"Вы ввели отрицательное целое число: {converted_number}"
        else:
            return f"Вы ввели не целое число: {input_string}"

    return wrapper


@validate_input
@is_positive_float
def analyze_and_convert_positive_float(input_string):
    converted_number = float(input_string)
    return f"Вы ввели положительное дробное число: {converted_number}"


@validate_input
@is_negative_float
def analyze_and_convert_negative_float(input_string):
    converted_number = float(input_string)
    return f"Вы ввели отрицательное дробное число: {converted_number}"


@validate_input
@is_positive_integer
def analyze_and_convert_positive_integer(input_string):
    converted_number = int(input_string)
    return f"Вы ввели положительное целое число: {converted_number}"


@validate_input
@is_negative_integer
def analyze_and_convert_negative_integer(input_string):
    converted_number = int(input_string)
    return f"Вы ввели отрицательное целое число: {converted_number}"


print(analyze_and_convert_negative_float("-6.7"))
print(analyze_and_convert_positive_integer("5"))
print(analyze_and_convert_positive_float("5.4"))
print(analyze_and_convert_negative_float("-0.777"))
print(analyze_and_convert_negative_integer("5.4r"))
print(analyze_and_convert_positive_integer("-5"))

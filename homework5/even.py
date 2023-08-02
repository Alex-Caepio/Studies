is_even_odd = lambda x: 'четное' if x % 2 == 0 else 'нечетное'

number1 = 10
number2 = 7

print(is_even_odd(number1))
print(is_even_odd(number2))

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: str(x), numbers))

print(result)

words = ('radar', 'python', 'level', 'hello', 'madam')

palindromes = tuple(filter(lambda word: word == word[::-1], words))

print(palindromes)

from datetime import datetime


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        milliseconds = execution_time.total_seconds() * 1000
        print(f"Время выполнения функции '{func.__name__}': {execution_time.seconds} секунд {milliseconds} миллисекунд")
        return result

    return wrapper


@measure_execution_time
def sum_list(numbers):
    return sum(numbers)


@measure_execution_time
def is_even(number):
    return number % 2 == 0


numbers_list = [1, 2, 3, 4, 5]

result = sum_list(numbers_list)
print(f"Сумма списка чисел: {result}")

number = 10
result = is_even(number)
print(f"Число {number} {'четное' if result else 'нечетное'}")


def analyze_and_convert(input_string):
    # Проверяем, является ли входная строка числом
    if input_string.lstrip('-').replace('.', '', 1).isdigit():
        # Если входная строка содержит точку, это дробное число
        if '.' in input_string:
            converted_number = float(input_string)
            if input_string.startswith('-'):
                return f"Вы ввели отрицательное дробное число: {converted_number}"
            else:
                return f"Вы ввели положительное дробное число: {converted_number}"
        # Если входная строка не содержит точку, это целое число
        else:
            converted_number = int(input_string)
            if input_string.startswith('-'):
                return f"Вы ввели отрицательное целое число: {converted_number}"
            else:
                return f"Вы ввели положительное целое число: {converted_number}"
    else:
        return f"Вы ввели некорректное число: {input_string}"


# Примеры использования:
print(analyze_and_convert("-6.7"))  # Вы ввели отрицательное дробное число: -6.7
print(analyze_and_convert("5"))  # Вы ввели положительное целое число: 5
print(analyze_and_convert("5.4r"))  # Вы ввели некорректное число: 5.4r
print(analyze_and_convert("-.777"))  # Вы ввели отрицательное дробное число: -0.777

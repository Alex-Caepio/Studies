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

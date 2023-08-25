class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        return a / b


OPERATION_DICT = {
    "+": Calculator.add,
    "-": Calculator.subtract,
    "*": Calculator.multiply,
    "/": Calculator.divide
}


class LengthOfTheIntegersError(Exception):
    def __init__(self, number, max_length):
        self.number = number
        self.max_length = max_length
        super().__init__(f"Length of the integer {number} is greater than {max_length}")


def check_integer_length(number, max_length=5):
    if len(str(number)) > max_length:
        raise LengthOfTheIntegersError(number, max_length)


try:
    num1 = float(input("Введите первое число: "))
    check_integer_length(num1)

    num2 = float(input("Введите второе число: "))
    check_integer_length(num2)

    operation = input("Введите операцию (+, -, *, /): ")

    if operation in OPERATION_DICT:
        result = OPERATION_DICT[operation](num1, num2)
        print("Результат:", result)
    else:
        print("Неверная операция")

except ValueError as ve:
    print("Неверное значение:", ve)
except ZeroDivisionError as zde:
    print("Ошибка: деление на ноль!", zde)
except LengthOfTheIntegersError as le:
    print(f"Ошибка: {le}")
except TypeError as te:
    print("Ошибка: некорректный тип данных!", te)
except EOFError as eof:
    print("Ошибка: неожиданный конец ввода!", eof)

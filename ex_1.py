from functools import reduce


def map_and_multiply_by_two(numbers: list) -> list:
    """
    Принимает список чисел и возвращает новый список, в котором каждое число увеличено на 10 и умножено на два, используя map.

    """
    processed_numbers = list(map(lambda x: x * 2 + 10, numbers))
    return processed_numbers


def filter_positive_values(numbers: list) -> list:
    """
    Принимает список чисел и возвращает новый список, в котором оставлены только отрицательные числа, используя filter.

    """
    positive_numbers = list(filter(lambda x: x < 0, numbers))
    return positive_numbers


def reduce_and_multiply_by_two(numbers: list) -> int:
    """
    Принимает список чисел и суммирует каждые 2 числа, а затем на каждой итерации умножает результат на 2, используя reduce.

    """
    summed_numbers = reduce(lambda x, y: x + y, numbers)
    multiplied_result = summed_numbers * 2
    return multiplied_result


my_list = [-3, 1, 2, 3, 4, 5, -10]

mapped_list = map_and_multiply_by_two(my_list)
print(mapped_list)

filtered_list = filter_positive_values(my_list)
print(filtered_list)

reduced_and_multiplied_result = reduce_and_multiply_by_two(my_list)
print(reduced_and_multiplied_result)

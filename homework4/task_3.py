from typing import List, Dict


def count_numbers(lst: List[int]) -> Dict[int, int]:
    number_count: Dict[int, int] = {}

    for number in lst:
        count: int = number_count.get(number, 0)

        count += 1

        number_count[number] = count

    return number_count


numbers_list: List[int] = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2]

result_dict: Dict[int, int] = count_numbers(numbers_list)

print(result_dict)

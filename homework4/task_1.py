from typing import Dict


def swap_keys_and_values(input_dict: Dict[str, int]) -> Dict[int, str]:
    swapped_dict: Dict[int, str] = {value: key for key, value in input_dict.items()}
    return swapped_dict


original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

swapped_dict = swap_keys_and_values(original_dict)

print(swapped_dict)

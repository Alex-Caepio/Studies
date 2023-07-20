from datetime import datetime
import time
from typing import List


def get_current_time() -> str:
    time.sleep(1)

    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


def generate_list_with_delay() -> List[str]:
    n = int(input("Введите количество элементов списка: "))

    return [get_current_time() for _ in range(n)]


result_list = generate_list_with_delay()

print(result_list)

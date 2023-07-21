import re
from datetime import datetime
from typing import Generator


def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


points_en = {1: 'AEIOULNSTR',
             2: 'DG',
             3: 'BCMP',
             4: 'FHVWY',
             5: 'K',
             8: 'JZ',
             10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ',
             2: 'ДКЛМПУ',
             3: 'БГЁЬЯ',
             4: 'ЙЫ',
             5: 'ЖЗХЦЧ',
             8: 'ШЭЮ',
             10: 'ФЩЪ'}
text = input("Введите текст: ").upper()

if (isCyrillic(text)):
    print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
    print(sum([k for i in text for k, v in points_en.items() if i in v]))


# points_list = []  # Создаем пустой список для хранения очков
#
# for i in text:  # Перебираем каждый символ i в тексте
#     for k, v in points_ru.items():  # Перебираем ключи k и значения v из словаря points_ru
#         if i in v:  # Проверяем, содержится ли символ i в значениях v словаря points_ru
#             points_list.append(k)  # Добавляем очки k в список points_list
#
# print(points_list)  # Выводим список очков

def get_current_time() -> Generator[str, None, None]:
    return (datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S') for _ in range(10))


print(list(get_current_time()))

def season(month):
    seasons = {
        1: ("Январь", "Зима"),
        2: ("Февраль", "Зима"),
        3: ("Март", "Весна"),
        4: ("Апрель", "Весна"),
        5: ("Май", "Весна"),
        6: ("Июнь", "Лето"),
        7: ("Июль", "Лето"),
        8: ("Август", "Лето"),
        9: ("Сентябрь", "Осень"),
        10: ("Октябрь", "Осень"),
        11: ("Ноябрь", "Осень"),
        12: ("Декабрь", "Зима")
    }
    month_name, season_name = seasons.get(month, ("Неверный номер месяца", "Пожалуйста, введите число от 1 до 12."))
    return f"Месяц: {month_name}, Время года: {season_name}"


print(season(3))
print(season(8))
print(season(13))


# Task 2

def calculate_power_sum(num1, num2, power=1):
    result = (num1 + num2) ** power
    return result


print(calculate_power_sum(2, 3))
print(calculate_power_sum(2, 3, 2))
print(calculate_power_sum(2, 3, 3))
print(calculate_power_sum(2, 3, 0.5))


# Task 3

def is_valid_date(day, month, year):
    if day < 1 or month < 1 or month > 12 or year < 1:
        return False

    max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > max_days[month - 1]:
        return False

    return True


print(is_valid_date(31, 1, 2023))
print(is_valid_date(29, 2, 2024))
print(is_valid_date(30, 2, 2023))
print(is_valid_date(31, 4, 2023))

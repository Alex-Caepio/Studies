import random
import os

number = random.randint(1, 20)

guesses = 0

while guesses <= 10:
    guess = int(input("Введите число от 1 до 20: "))

    guesses += 1

    if guess == number:
        print("Вы угадали! Число было", number)
        break
    elif guess < number:
        print("Ваше число меньше загаданного")
    else:
        print("Ваше число больше загаданного")

if guesses > 10:
    folder_name = f"Looser{str(number)}"

    os.makedirs(folder_name, exist_ok=True)
    print(f"Папка успешно создана: {folder_name}")

# while

n = int(input("Введите целое число: "))

sum = 0
i = 1
while i <= n:
    sum += i ** 3
    i += 1

print("Сумма кубов всех целых чисел от 1 до n равна", sum)

# for

n = int(input("Введите целое число: "))
sum = 0

for i in range(1, n + 1):
    sum += i ** 3

print("Сумма кубов всех целых чисел от 1 до n равна", sum)

# Task 1
data = [1, 2, 3]

var1 = data
var2 = data
var3 = data

print(var1)
print(var2)
print(var3)

print(id(var1))
print(id(var2))
print(id(var3))

# Task 2
data = [1, 2, 3]

var4 = list(data)
var5 = list(data)

print(var4)
print(var5)

print(id(var4))
print(id(var5))

# Task 3
data = [1, 2, 3]
var1 = list(data)
var2 = list(data)
var3 = list(data)

var4 = data
var5 = data

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

print(id(var1))
print(id(var2))
print(id(var3))
print(id(var4))
print(id(var5))

# Task 4
input_string = input("Введите произвольную строку: ")

input_string = input_string.strip()

even_chars = input_string[::2]
odd_chars = input_string[1::2]

print("Введена строка:", input_string)
print("\n\n")

print(even_chars, odd_chars, sep="     ", end="\n!!!\n")

a = [1, 2, 3]
b = a
b[0] = 4
print(a)
print(id(a))
print(id(b))

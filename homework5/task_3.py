words = ('radar', 'python', 'level', 'hello', 'madam')

palindromes = tuple(filter(lambda word: word == word[::-1], words))

print(palindromes)

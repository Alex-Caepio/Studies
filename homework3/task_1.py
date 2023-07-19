# Task 1

sentence = input("Введите предложение из двух слов: ")
word1, word2 = sentence.split()

formatted_sentence = "! %s ! %s !" % (word2, word1)
print(formatted_sentence)

sentence = input("Введите предложение из двух слов: ")
word1, word2 = sentence.split()

formatted_sentence = "! {} ! {} !".format(word2, word1)
print(formatted_sentence)

sentence = input("Введите предложение из двух слов: ")
word1, word2 = sentence.split()

formatted_sentence = f"! {word2} ! {word1} !"
print(formatted_sentence)

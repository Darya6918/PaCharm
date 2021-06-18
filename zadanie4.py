# Вводим 3 произвольных слова. Пусть будет название овощей.
# Выводим все 3 слова с нижнем регистре, в верхнем регистре, потом только первый сивол в верхний -
# -(есть отдельная функция для этого)
# Далее вводим кол-во каждого овоща.
# После чего с помощью метода format выводим все данные в читаемом виде.

word1 = input("1 овощ: ")
word2 = input("2 овощ: ")
word3 = input("3 овощ: ")
lower1 = word1.lower()
lower2 = word2.lower()
lower3 = word3.lower()
upper1 = word1.upper()
upper2 = word2.upper()
upper3 = word3.upper()
title1 = word1.title()
title2 = word2.title()
title3 = word3.title()
words1 = int(input("сколько " + word1 + ": "))
words2 = int(input("сколько " + word2 + ": "))
words3 = int(input("сколько " + word3 + ": "))
print("{} ({}, {}, {})".format(words1, lower1, upper1, title1))
print("{} ({}, {}, {})".format(words2, lower2, upper2, title2))
print("{} ({}, {}, {})".format(words3, lower3, upper3, title3))

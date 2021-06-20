# Переделываем задачу номер  4 на функции.

def wordLower(name):
    return name.lower()
def wordUpper(name):
    return name.upper()
def wordTitle(name):
    return name.title()
def sum(count):
    return count

word1 = input("1 овощ: ")
word2 = input("2 овощ: ")
word3 = input("3 овощ: ")

words1 = int(input("сколько " + word1 + ": "))
words2 = int(input("сколько " + word2 + ": "))
words3 = int(input("сколько " + word3 + ": "))

print("{} ({}, {}, {})".format(sum(words1), wordLower(word1), wordUpper(word1), wordTitle(word1)))
print("{} ({}, {}, {})".format(sum(words2), wordLower(word2), wordUpper(word2), wordTitle(word2)))
print("{} ({}, {}, {})".format(sum(words3), wordLower(word3), wordUpper(word3), wordTitle(word3)))

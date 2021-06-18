import math
import random

# 3
# Написать мини калькулятор.
# В консоле ожидается ввод того сивола, операцию которую мы будем выполнять.
# Операцции: +, -, /, *, Возведение в степень, модуль, рандомное число, факториал и пусть будет арккосинус.
# Далее в консоль вводится столько значений, сколько требуется для операции. Для рандомного например 0.
# И выводим значение.

operator = input("ввести арифметический оператор: ")
if operator == "+":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a + b)
elif operator == "-":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a - b)
elif operator == "/":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a / b)
elif operator == "*":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a * b)
elif operator == "pow":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(pow(a, b))
elif operator == "module":
    a = float(input("ввести значение: "))
    print(abs(a))
elif operator == "div":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a // b)
elif operator == "mod":
    a = float(input("ввести 1 значение: "))
    b = float(input("ввести 2 значение: "))
    print(a % b)
elif operator == "f":
    a = int(input("ввести  значение: "))
    print(math.factorial(a))
elif operator == "arccos":
    a = float(input("ввести значение: "))
    b = a * math.pi / 180
    print(math.acos(b))
elif operator == "0":  # операция рандомное число, если нажать на ноль
    print(random.randint(0, 1000))
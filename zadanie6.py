# 6.
# Переделываем задачу номер 3(калькулятор) и номер 5 на функции.
import math
import random


def plus (a1, b2):
    return a1 + b2

def minus(a1, b2):
    return a1 - b2

def div(a1, b2):
    if b2 != 0:
        return a1 / b2
    else:
        print("на 0 не делиться")

def multi(a1, b2):
    return a1 * b2

def pow(a1,b2):
    return math.pow(a1, b2)

def module(a1):
    return abs(a1)

def whole_div(a1,b2):
    if b2 !=0:
        return a1//b2
    else:
        ptint("на 0 не делиться")

def mod(a1, b2):
    return (a1 % b2)

def factorial(a1):
    return math.factorial(a1)
def arccos(a1):
    return a1*math.pi/180

def rand(a1,b2):
    return random.uniform(a1,b2)

do = input("ввести арифметический оператор:")
while do !="exit":
    if do == "+":
        print(plus(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="-":
        print(minus(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="/":
        print(div(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="*":
        print(multi(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="^":
        print(pow(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="module":
        print(module(a1=float(input("ввести 1 значение:"))))

    elif do =="//":
        print(whole_div(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="%":
        print(mod(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="f":
        print(factorial(a1=int(input("ввести 1 значение:"))))

    elif do =="arccos":
        print(math.acos(arccos(a1=float(input("ввести значение:")))))

    elif do == "0":
        print(rand(a1=float(input("ввести верхнее значение:")), b2=float(input("ввести нижнее значение:"))))

    do = input("Введите оператор:")


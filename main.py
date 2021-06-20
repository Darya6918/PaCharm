# Сделать из функций калькулятора отдельный класс.

import math
import random

class Calculator:
    def plus(self, a1, b2):
        return a1 + b2

    def minus(self, a1, b2):
        return a1 - b2

    def div(self,a1, b2):
        if b2 != 0:
            return a1 / b2
        else:
            print("на 0 не делиться")

    def multi(self, a1, b2):
        return a1 * b2

    def pow(self, a1, b2):
        return math.pow(a1, b2)

    def module(self, a1):
        return abs(a1)

    def whole_div(self, a1,b2):
        if b2 !=0:
            return a1//b2
        else:
            print("на 0 не делиться")

    def mod(self, a1, b2):
        return (a1 % b2)

    def factorial(self, a1):
        return math.factorial(a1)

    def arccos(self, a1):
        return a1*math.pi/180

    def rand(self, a1, b2):
        return random.uniform(a1, b2)

calc = Calculator()
do = input("ввести арифметический оператор:")
while do !="exit":
    if do == "+":
        print(calc.plus(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="-":
        print(calc.minus(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="/":
        print(calc.div(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="*":
        print(calc.multi(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="^":
        print(calc.pow(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="module":
        print(calc.module(a1=float(input("ввести 1 значение:"))))

    elif do =="//":
        print(calc.whole_div(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="%":
        print(calc.mod(a1=float(input("ввести 1 значение:")), b2=float(input("ввести 2 значение:"))))

    elif do =="f":
        print(calc.factorial(a1=int(input("ввести 1 значение:"))))

    elif do =="arccos":
        print(math.acos(calc.arccos(a1=float(input("ввести значение:")))))

    elif do == "0":
        print(calc.rand(a1=float(input("ввести верхнее значение:")), b2=float(input("ввести нижнее значение:"))))

    do = input("Введите оператор:")

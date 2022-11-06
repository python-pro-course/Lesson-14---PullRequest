import math
znak = input("введите знак(если корень пишите 'корень'):")
if znak == "-":
    print(int(input()) - int(input()))
if znak == "+":
    print(int(input()) + int(input()))
if znak == "//":
    print(int(input()) // int(input()))
if znak == "%":
    print(int(input()) % int(input()))
if znak == "*":
    print(int(input()) * int(input()))
if znak == "**":
    print(int(input()) ** int(input()))
if znak == "корень":
    print(math.sqrt(int(input())))
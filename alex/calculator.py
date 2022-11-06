while True:
    import math

    znak = input("введите знак(если корень пишите 'корень', если логарифм пишите: 'логарифм'):")
    if znak == "корень":
        a = int(input())
    else:
        a = int(input())
        b = int(input())
    if znak == "-":
        print(f"разность чисел {a} и {b} = {a - b}")
    if znak == "+":
        print(f"сумма чисел {a} и {b} = {a + b}")
    if znak == "//":
        print(f"целочисленное деление {a} на {b} = {a // b}")
    if znak == "%":
        print(f"остаток от деления {a} на {b} = {a - b}")
    if znak == "*":
        print(f"сумма чисел {a} и {b} = {a - b}")
    if znak == "**":
        print(f"сумма чисел {a} и {b} = {a - b}")
    if znak == "корень":
        print(math.sqrt(int(input())))
    if znak == "логарифм":
        print(math.log(b, a))
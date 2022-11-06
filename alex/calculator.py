import math

calc = open("calculator_history.txt", "w")
while True:

    znak = input("введите знак(если корень пишите 'корень', если логарифм пишите: 'логарифм'):")
    if znak == "корень":
        a = int(input())
    else:
        a = int(input())
        b = int(input())
    if znak == "-":
        print(f"разность чисел {a} и {b} = {a - b}")
        calc.write(f"разность чисел {a} и {b} = {a - b}" + "\n")

    if znak == "+":
        print(f"сумма чисел {a} и {b} = {a + b}")
        calc.write(f"сумма чисел {a} и {b} = {a + b}" + "\n")

    if znak == "//":
        print(f"целочисленное деление {a} на {b} = {a // b}")
        calc.write(f"целочисленное деление {a} на {b} = {a // b}" + "\n")

    if znak == "%":
        print(f"остаток от деления {a} на {b} = {a - b}")
        calc.write(f"остаток от деления {a} на {b} = {a - b}" + "\n")

    if znak == "*":
        print(f"сумма чисел {a} и {b} = {a - b}")
        calc.write(f"сумма чисел {a} и {b} = {a - b}" + "\n")

    if znak == "**":
        print(f"сумма чисел {a} и {b} = {a - b}")
        calc.write(f"сумма чисел {a} и {b} = {a - b}" + "\n")

    if znak == "корень":
        print(f"корень из {a} = {math.sqrt(a)}")
        calc.write(f"корень из {a} = {math.sqrt(a)}" + "\n")

    if znak == "логарифм":
        print(f"я не знаю как правильно сформулировать так что вот вам ваш логарифм: {math.log(b, a)}")
        calc.write(f"я не знаю как правильно сформулировать так что вот вам ваш логарифм: {math.log(b, a)}")


def plus(first, second):
    print(int(first) + int(second))

def minus(first, second):
    print(int(first) - int(second))

def deff(first, second):
    print(int(first) * int(second))

def diff(first, second):
    if int(first) % int(second) == 0:
        print(int(int(first) / int(second)))
    if int(first) % int(second) != 0:
        print(int(first) / int(second))

def fulldiff(first, second):
    print(int(int(first) / int(second)))

def ostatok(first, second):
    ferst = (int(int(first) / int(second))) * int(second)
    sicond = int(first) / int(second) * int(second)
    print(int(sicond - ferst))

def stepen(first, second):
    print(int(first) ** int(second))

def root2(ok, index):
    d = 0
    if int(index) == 2:
        for i in range(1, int(ok) + 1):
            for ii in range(1, int(ok) + 1):
                if i * ii == int(ok) and i == ii:
                    d = i

    if int(index) == 3:
        for i in range(1, int(ok) + 1):
            for ii in range(1, int(ok) + 1):
                for iii in range(1, int(ok) + 1):
                    if i * ii * iii == int(ok) and i == ii == iii:
                        d = i

    if int(index) == 4:
        for i in range(1, int(ok) + 1):
            for ii in range(1, int(ok) + 1):
                for iii in range(1, int(ok) + 1):
                    for iiii in range(1, int(ok) + 1):
                        if i * ii * iii * iiii == int(ok) and i == ii == iii == iiii:
                            d = i
    if int(index) > 4:
        print("Функция пока недоступна")
    elif d != 0:
        print(d)
    elif d == 0:
        print("КОРНЕЙ НЕТ")

def logo(x, y):
    p = 0
    while x >= y:
        p += 1
        x /= y
    if x == 1:
        print(p)
    else:
        print("КОРНЕЙ НЕТ")





# Main part
print("                 Мой первый калькулятор!")
print("   Числа и знаки вводятся через пробел, иначе - поломка")
print("(<число> V n  -- корень n-ной степени от <числа> при n < 5)")
print("____________________________________________________________")

a, b, c = input().split()
print("~~~~~~~~~~~~")
printresult = True
while a and b and c != '':





    if printresult == True:
        if b == '+':
            plus(a, c)

        if b == '-':
            minus(a, c)

        if b == '*':
            deff(a, c)

        if b == '/':
            diff(a, c)

        if b == '//':
            fulldiff(a, c)

        if b == '%':
            ostatok(a, c)

        if b == '**':
            stepen(a, c)

        if b == 'V':
            root2(a, c)

        if b == 'log':
            logo(int(a), int(c))

    #elif b != 'V' or '**' or '/' or '%' or '//' or '*' or '-' or '+' or 'log':
     #   print("Функция пока недоступна")

    print("~~~~~~~~~~~~")
    key = 0
    printresult = True
    val = input()
    print("~~~~~~~~~~~~")
    for i in range(len(val)):
        if val[i] == ' ':
            key += 1
    if key == 2:
        a, b, c = val.split()

    else:
        print('Ошибка')
        printresult = False




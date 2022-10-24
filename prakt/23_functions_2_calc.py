# калькулятор

def summ(a, b):
    return a + b
def razn(a, b):
    return a - b
def umn(a, b):
    return a * b
def delen(a, b):
    return a / b

while True:
    a = int(input('Первое число: '))
    c = input('Действие: ')
    b = int(input('Второе число: '))

    if c == '+':
        print(summ(a, b))
    elif c == '-':
        print(razn(a, b))
    elif c == '*':
        print(umn(a, b))
    elif c == '/':
        print(delen(a, b))
    elif c == '0':
        break

# Практика. Переписать в лямбда выражение

summ = lambda a,b :a + b
razn = lambda a,b :a - b
umn = lambda a,b :a * b
delen = lambda a,b :a / b

while True:
    a = int(input('Первое число: '))
    c = input('Действие: ')
    b = int(input('Второе число: '))

    if c == '+':
        print(summ(a, b))
    elif c == '-':
        print(razn(a, b))
    elif c == '*':
        print(umn(a, b))
    elif c == '/':
        print(delen(a, b))
    elif c == '0':
        break
# Найти сумму цифр числа с помощью рекурсии. 112 = 4

x = int(input('Введи число: '))

def bip(x):
    if x == 0:
        return 0
    else:
        return x % 10 + bip(x // 10)
print(bip(x))
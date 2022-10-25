# рекурсивная ф-я возвращает результат возведения действительного числа х в целую степень у

x = int(input('Число: '))
y = int(input('Степень: '))

def One(x, y):
    if y > 0:
        return x*(One(x, y - 1))
    else:
        return 1
print(One(x, y))
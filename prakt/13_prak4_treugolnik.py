# Пользователь вводит высоту треугольника. Нужно построить прямоугольный треугольник

h = int(input('Введи высоту треугольника: '))
for i in range(1, h+1):
    for j in range(i):
        print('|\\', end = '')
    print()                     # ставим принт, чтобы был перенос строк
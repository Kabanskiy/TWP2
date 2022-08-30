# Пользователь вводит число n. Необходимо вывести все совершенные числа до n

chislo = int(input('Введи число: '))
for i in range(1, chislo+1):
    summ = 0
    for a in range(1, i):
        if i % a == 0:
            summ += a
    if i == summ:
        print('число', i, 'совершенное')

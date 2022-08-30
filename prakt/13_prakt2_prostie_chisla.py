# Пользователь вводит число n. Необходимо вывести все простые числа до n

n = int(input('Введи число: '))
for i in range(1, n):
    summ = 0
    for a in range(1, i+1):
        if i % a == 0:
            summ += a
    if i + 1 == summ:
        print(i, ' - простое число')
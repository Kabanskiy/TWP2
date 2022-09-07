# Найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

chis = input('Введи число: ')

summ = 0
ma = 0
mi = 0

for i in chis:
    if i == max(chis):
        ma += int(i)
    if i == min(chis):
        mi += int(i)

for i in range(mi+1, ma, 1):
    summ += int(i)
print(summ)
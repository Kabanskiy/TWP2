# на вход приходит случайное 10значное число. Нужно посчитать сумму его цифр

import random

num = random.randint(1000000000, 9999999999)
print(num)
summ = 0

for i in str(num):
    summ += int(i)
print(summ)

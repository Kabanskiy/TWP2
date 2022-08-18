# 1. Придумать и обработать исключения на TypeError и ValueError.
# 2. Известны год, номер месяца и день рождения человека, а также день, год и номер месяца сегодняшнего дня. Определите возраст человека (число полных лет).

#1
# try:
#   primer = 100 + 'Vasya'
# except TypeError:
#     print('Несовместимые типы')
#
# try:
#     primer = 100 + int('Vasya')
# except ValueError:
#     print('Неверное значение')

# 2
date_old = int(input('Введи дату рождения: '))
month_old = int(input('Введи месяц рождения: '))
year_old = int(input('Введи год рождения: '))

date_new = int(input('Введи сегодняшнюю дату: '))
month_new = int(input('Введи сегодняшний месяц: '))
year_new = int(input('Введи сегодняшний год: '))

old = year_new - year_old
months = month_new - month_old
days = date_new - date_old

print(f'Ваш полный возраст {(old * 12 + months + days)// 12} лет')


# Известны год, номер месяца и день рождения каждого из двух человек. Определить, кто из них старше.

date1 = int(input('Введи дату рождения первого: '))
month1 = int(input('Введи месяц рождения первого: '))
year1 = int(input('Введи год рождения первого: '))

date2 = int(input('Введи дату рождения второго: '))
month2 = int(input('Введи месяц рождения второго: '))
year2 = int(input('Введи год рождения второго: '))

if year1 < year2:
    print('Первый старше')
elif year1 == year2 and month1 < month2:
    print('Первый старше')
elif year1 == year2 and month1 == month2 and date1 < date2:
    print('Первый старше')
else:
    print('Второй старше')

# 1. В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
#1
f = open('spis_clas2.txt', 'w')
f.write('Ivan Ivanov 1\nPetr Petrov 2\nVasiliy Vasiliev 4\nBoris Borisov 4\nAnton Antonov 3')
f.close()

c = 0
with open('spis_clas2.txt', 'r') as f:
    sp = f.readlines()
    for i in sp:
        i.replace('\n', '')
        i = i.split()
        c += int(i[2])
        if int(i[2])<3:
            print(f'{i[0]} {i[1]} {i[2]}')
    print()
    print(f'Средний балл: {c/len(sp)}')
#2
f = open('dannie.txt','w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
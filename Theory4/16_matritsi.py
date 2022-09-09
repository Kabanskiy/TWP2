# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)
#
# list2 = []
# for i in range(10):
#     list2.append([10, 20, 30, 40])
# print(list2)

list3 = []
n = int(input('Введи количество строк матрицы: '))
m = int(input('Введи количество столбов матрицы: '))
for i in range(n):
    list3_1 = []
    for j in range(m):
        a = int(input('Введите элементы: '))
        list3_1.append(a)
    list3.append(list3_1)
for i in list3:                     # вывод таблички
    print(i)
# 1. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# 2. Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

#1
import random
mas = [random.randint(1, 100) for i in range(10)]
print(sorted(mas))
n1 = min(mas)
print(n1)
mas.remove(n1)
n2 = min(mas)
print(n2)

print('задача 2:')

b = int(input('Диапазон от: '))
c = int(input('Диапазон до: '))
del mas[b:c]
print(mas)
k = len(mas[b:c])
mas.append((0)*k)
print(mas)
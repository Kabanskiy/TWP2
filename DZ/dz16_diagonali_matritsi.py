# 1. Найти максимальный элемент диагонали матрицы.
# 2. Вычислить количество отрицательных элементов под главной диагональю матрицы.

spisok = [[1, 2, -3],
          [4, 5, 6],
          [-7, 8, 9]]
one = 0
two = -1
numbers = []
menshe_0_ = 0
for i in range(len(spisok)):
    numbers.append(spisok[one][two])
    if spisok[one][two] < 0:
        menshe_0_ +=1
    one += 1
    two -= 1
print(f'максимальное число диагонали: ',max(numbers))
print(f'Чисел меньше 0: ', menshe_0_)
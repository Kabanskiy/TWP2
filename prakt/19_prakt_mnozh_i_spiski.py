# польз-ль вводит значения в список. Нужно оставить только уникальные элементы в этом списке и отсортировать его

n = int(input('Введи длину списка: '))
list_one = [] # создаем пустой список для хранения элементов, введенных пользователем
# создаем цикл для добавления элементов в этот список:
for i in range(n):
    list_one.append(input(''))  # каждый проход мы будем передавать значения
list_one = list(set(list_one)) # переводим в множество, т.к. оно содержит только уникальные элементы и возвр в список
list_one.sort() # сортируем не в принте т.к. сорт - это метод
print(list_one)
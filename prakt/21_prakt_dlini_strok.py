# Вывести длину каждой строки файла, в котором несколько строк

with open('spis_clas2.txt', 'r') as f:
    spisok1 = f.readlines() # вместо того, чтобы принтить весь список, загоним его в переменную
    for i in spisok1:
        print(len(i.replace('\n', ''))) # печатаеим без переноса, т.к. с ним кол-во будет неправильно
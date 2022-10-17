# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество символов и слов в ней.

with open('spis_clas2.txt', 'r') as f:
    strok = 0
    for i in f:
        strok += 1
        simv = 0
        slov = 0
        for j in i:
            if j != ' ' and simv == 0:
                slov += 1
                simv = 1
            elif j == ' ':
                simv = 0
        print('Символов: ', len(i.replace('\n', '')), 'Слов: ', slov)
    print('Строк: ', strok)

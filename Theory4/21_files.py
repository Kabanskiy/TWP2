# w - запись, r - чтение, a - дозапись

# f = open('name_file1.txt', 'r')
# f.write('zdarov\nhey') # во write обычная строка
# f.writelines(['sdfss\n', 'dgdgsgdg\n', 'sdfsfsf']) # во writelines можно список
# print(f.read(7)) # читает только первые 7 симолов
# print(f.readline()) # читает только первую строку в файле. Если написать еще раз, выведет вторую
# print(f.readlines()) # выводит список всех строк
# f.close()

# with open('name_file1.txt', 'a') as f: # эта конструкция будет выполнятся при вызове f
#     f.write('\nbababam')
# закрывать здесь не нужно

with open('name_file1.txt', 'r') as f: # чтение через цикл
    for i in f:
        print(i)
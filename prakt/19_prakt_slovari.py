# польз-ль вводит слово. нужно вывести его перевод с рус на англ и наоборот. Слова с переводом хранятся в словаре
dict_one = {
    'one':'один',
    'two':'два',
    'three':'три'
}

stroka = input('ВВеди слово: ')
for key,val in dict_one.items():
    if stroka == key:
        print(val)
    elif stroka == val:
        print(key)
else:
    print('нет в словаре')
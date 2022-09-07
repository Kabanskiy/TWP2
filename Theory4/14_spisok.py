spisok = (2, None, 'Dorou', True) # тип list
for i in spisok:
    try:
        print(i+1)
        # True = 1     так принято
        # False = 0
    except TypeError:
        print('Ошибка типа')

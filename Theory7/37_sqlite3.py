import sqlite3

#  чтобы подключиться к базе, нужно создать команду и указать название в ковычках/ И обязательно открыть курсор

conn = sqlite3.connect('databae.db') # открыаем соединение с базой данных
curs = conn.cursor() # создаем курсор, он будет взаимодействовать с нашей базой, создавать таблицы, данные и т.д.

zapros1 = """CREATE TABLE IF NOT EXISTS tablitsa1(login TEXT, password TEXT);"""
# вставляем IF NOT EXISTS чтобы не было ошибки "таблиа уже создана"
curs.execute(zapros1) # создаем запрос
conn.commit() # комитим для сохранени базы


# запрос для заполнения данных с таблицу
zapros2 = """INSERT INTO tablitsa1(login, password) VALUES ('Uassya', '100500');"""
# чтобы применялось ко всем полям, можно не ставить "(login, password)"
curs.execute(zapros2)
conn.commit()

# также можно добавлять данные через кортеж
tuple1 = ('Ivan', '2222')
zapros3 = """INSERT INTO tablitsa1 VALUES (?, ?);""" # на место букв ставим "?"
curs.execute(zapros3, tuple1) # и ставим название списка или кортежа из которого добавляем
conn.commit()


curs.close() # после отработки обязательно закрываем методом close
conn.close() # после отработки обязательно закрываем методом close
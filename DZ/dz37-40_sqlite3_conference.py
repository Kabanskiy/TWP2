# 37: Создать базу данных фирмы, обслуживающей конференции.
# БД должна содержать:
# - справочник персоналий участников конференции (Ф.И.О., ученая степень, научное направление, место работы, кафедра,
# должность, страна, город, адрес, рабочий телефон, адрес электронной почты);
# - информацию, связанную с участием в конференции (докладчик или участник, дата рассылки приглашения,
# дата поступления заявки, тема доклада, отметка о поступлении тезисов, дата приезда, потребность в гостинице, дата отъезда).
# В БД необходимо хранить следующую информацию о конференции:
# - название конференции;
# - дата проведения;
# - место проведения;
# - организаторы;
# - спонсоры;
# - количество дней проведения конференции;
# - количество участников;
# - количество докладчиков.


# 38: Заполните таблицы из предыдущего занятия данными (минимум шесть записей на каждую таблицу).
# 39: Вывести данные из таблицы, созданной на предыдущем уроке.
# Вывод всех данных из таблицы и вывод из таблицы данных подчиняющихся какому-то условию.
# 40: В вашей БД из предыдущего занятия удалите половину записей. А вторую половину измените
import sqlite3

conn = sqlite3.connect('dz37_sqlite3.db')
cursor = conn.cursor()

zapros_conference = """CREATE TABLE IF NOT EXISTS Conference(name TEXT, date TEXT, location TEXT, organisators TEXT, sponsors TEXT,
whats_days TEXT, whats_speakers TEXT, kol_speakers TEXT);"""
cursor.execute(zapros_conference)
conn.commit()

# zapros_conference_2 = """INSERT INTO Conference VALUES('Vasya', '22.11.', 'universitet', 'Ivan da Marya', 'Mark Formele', '3 days', 'Timofei', '2');"""
# cursor.execute(zapros_conference_2)
# conn.commit()
#
# zapros_conference_3 = """INSERT INTO Conference VALUES('Ura', '23.11.', 'universitet', 'Marya da Ivan', 'Rogachev', '1 day', 'Uassya', '2');"""
# cursor.execute(zapros_conference_3)
# conn.commit()
#
# zapros_conference_4 = """INSERT INTO Conference VALUES('Chuck Norris', '28.11.', 'academy', 'Ignat', 'Kolbasa', '1 day', 'Olga', '1');"""
# cursor.execute(zapros_conference_4)
# conn.commit()
#
# zapros_conference_5 = """INSERT INTO Conference VALUES('Jackey Chan', '30.11.', 'college', 'Nikolay', 'MTZ', '2 days', 'Li', '1');"""
# cursor.execute(zapros_conference_5)
# conn.commit()
#
# zapros_conference_6 = """INSERT INTO Conference VALUES('Shcwarznegger', '03.12.', 'academy', 'Yarek', 'BELAZ', '1 day', 'Luka', '1');"""
# cursor.execute(zapros_conference_6)
# conn.commit()
# zapros_conference_del = """DELETE FROM Conference WHERE location='universitet';"""
# cursor.execute(zapros_conference_del)
# conn.commit()

zapros_spravochnik = """CREATE TABLE IF NOT EXISTS Personalii (FIO TEXT, stepen TEXT, science_way TEXT, job TEXT, kafedra TEXT, dolzhnost TEXT,
country TEXT, city TEXT, adress TEXT, phone TINYINT, mail TEXT);"""
cursor.execute(zapros_spravochnik)
conn.commit()

zapros_spravochnik_up = """UPDATE Personalii SET stepen='professional' WHERE stepen='rabotyaga';"""
cursor.execute(zapros_spravochnik_up)
conn.commit()

# tuple2 = ('Chuck Norris', 'docent', 'theckvandology', 'karate', 'dzudovedenie', 'coach', 'USA', 'Texas', 'Holliwood st.', '+100500', 'chuck@norris')
# zapros_spravochnik2 = """INSERT INTO Personalii VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_spravochnik2, tuple2)
# conn.commit()
#
# tuple3 = ('Jackey Chan', 'docent', 'trukology', 'karate', 'kikusikai', 'coach', 'China', 'Pekin', 'Sin Su An', '+1111555', 'jackey@chan')
# zapros_spravochnik3 = """INSERT INTO Personalii VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_spravochnik3, tuple3)
# conn.commit()
#
# tuple4 = ('Afanasy Perdunov', 'rabotyaga', 'mehanica', 'tractorist', 'materialovedenie', 'student', 'Belarus', 'Brest', 'vul Sovetskaya', '+375500', 'afonya@tractor')
# zapros_spravochnik4 = """INSERT INTO Personalii VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_spravochnik2, tuple4)
# conn.commit()
#
# tuple5 = ('Ivan Dulin', 'rabotyaga', 'frezerovka', 'frezerovshik', 'stankovedenie', 'rabochii', 'Russia', 'Chelyabinsk', 'ul Lenina', '+790500', 'ivan@dulin')
# zapros_spravochnik5 = """INSERT INTO Personalii VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_spravochnik5, tuple5)
# conn.commit()
#
# tuple6 = ('Alexandr Pushkin', 'poet', 'stikhotvorshina', 'pisatel', 'literatura', 'coach', 'Russia', 'St. Petersburg', 'ul. Moyka', '-', 'golub')
# zapros_spravochnik6 = """INSERT INTO Personalii VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_spravochnik6, tuple6)
# conn.commit()

zapros_infa = """CREATE TABLE IF NOT EXISTS Spikers(speaker TEXT, date_rssilki DATE, date_zayavki DATE, theme TEXT, otmetka TEXT, 
date_zezda DATE, hotels_need TEXT, date_viezda DATE);"""
cursor.execute(zapros_infa)
conn.commit()

# zapros_viborka = """SELECT * FROM Spikers;"""
# cursor.execute(zapros_viborka)
# a = cursor.fetchall()
# print(a)
#
# zapros_viborka2 = """SELECT * FROM Spikers WHERE speaker = 'Diogen';"""
# cursor.execute(zapros_viborka2)
# b = cursor.fetchall()
# print(b)

# spisok2 = ['Neznaika', '22.11', '01.11.', 'Luna', 'yes', '23.11.', 'grusheviy sad', '25.11.']
# zapros_infa_2 = """INSERT INTO Spikers VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_infa_2, spisok2)
# conn.commit()
#
# spisok3 = ['Yoseph Gebelts', '19.10.37', '01.09.1939', 'Nazional Socialism', 'ya', '22.06.1941', 'reihskanelyarya', '09.05.1945']
# zapros_infa_3 = """INSERT INTO Spikers VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_infa_3, spisok3)
# conn.commit()
#
# spisok4 = ['Michael Shcumakher', '20.03.83', '11.08.1985', 'Formula 1', 'no', '-', 'gonka', '-']
# zapros_infa_4 = """INSERT INTO Spikers VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_infa_4, spisok4)
# conn.commit()
#
# spisok5 = ['Eis Ventura', '10.01.1993', '20.04.1993', 'Animals', 'yes', '20.05.1993', 'konsulstvo', '29.05.1993']
# zapros_infa_5 = """INSERT INTO Spikers VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_infa_5, spisok5)
# conn.commit()
#
# spisok6 = ['Diogen', '2000', '1999', 'Philosophy', 'nein', '-', 'Bochka', '-']
# zapros_infa_6 = """INSERT INTO Spikers VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""
# cursor.execute(zapros_infa_6, spisok6)
# conn.commit()

cursor.close()
conn.close()

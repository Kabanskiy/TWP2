import json

# для чтения
# with open('22_json.json') as f: # для чтения режим указывать не обязательно
#     tuk = json.load(f) # функция load считывает инфу с файла '22_json.json' и записывает в переменную tuk
# print(tuk) # выводится словарь. К которому можно обратиться даже по ключу tuk[name] => Yarek


# для записи
# для начала записыаем словарь, который будем сохранять в файл (ключ вседа это строка или кортеж):
dict1= {
    "street": "pervomayka",
    "house": 2,
    "appatament": 2
}
with open('22_json.json', 'w') as f: #здесь уже указываем режим записи соответственно
    json.dump(dict1, f, indent=2, sort_keys=True) # указываем название словаря и файла. indent=2 - параметр,
    # переносящий ключи на 2 пробела. sort_keys - сортирует ключи в алфавитном порядке

# файл не может хранить срзу два словаря в одном файле
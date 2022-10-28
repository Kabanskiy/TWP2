# Создать класс и вызвать пять объектов этого класса.

class Heroes:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def present(self):
        print('Самый крутой - ' + self.name + ' ' + self.surname)

hero1 = Heroes('Чак', 'Норрис')
hero1.present()
hero2 = Heroes('Джеки', 'Чан')
hero2.present()
hero3 = Heroes('Арни', 'Шварцниггер')
hero3.present()
hero4 = Heroes('Жан-клод', 'Ван-дамм')
hero4.present()
hero5 = Heroes('Брюс', 'Вылез')
hero5.present()
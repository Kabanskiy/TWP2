class Chuvak:
    def __init__(self, age, name): # конструктор
        self.age = age
        self.name = name
    def muzhik(self): # метод
        print('дороу ' + self.name + ' тебе лет ' + str(self.age))

human = Chuvak(30, 'Уасся')
human.muzhik()
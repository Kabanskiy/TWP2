class Mashina():
    def __init__(self, model = 'Q5', marka = 'Audi'):
        self.model = model
        self.marka = marka

    def info(self):
        print('Модель: ' + self.model + ', Марка: ' + self.marka)

class Toyota(Mashina):
    def __init__(self, model):
        self.model = model
    def info(self):
        print('Модель: ' + self.model)


car = Mashina(model = 'G500', marka = 'Mercedes') # если в начале стоят значиения по умолчанию, то можно изменить здесь
car.info()

to = Toyota('tundra')
to.info()


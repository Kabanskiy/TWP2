class Mashina():
    def __init__(self, model, marka):
        self.model = model
        self.marka = marka

    def info(self):
        print('Модель: ' + self.model + ', Марка: ' + self.marka)

class Toyota(Mashina):
    def __init__(self, model):
        self.model = model
    def info(self):
        print('Модель: ' + self.model)

to = Toyota('tundra')
to.info()

car = Mashina('camry', 'toyota')
car.info()

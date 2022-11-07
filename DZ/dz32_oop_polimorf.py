# В наследниках класса из предыдущего урока переопределить методы из класса родителя,
# а также добавить не менее трёх значений по умолчанию.

class Mashina():
    def __init__(self, model = 'Q5', marka = 'Audi', year = '2020'):
        self.model = model
        self.marka = marka
        self.year = year

    def info(self):
        print('Модель: ' + self.model + ', Марка: ' + self.marka + ', Год выпуска: ' + self.year)

class Toyota(Mashina):
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def info(self):
        print('Модель: ' + self.model + ', Год выпуска: ' + self.year)

car = Mashina(model = 'G500', marka = 'Mercedes', year = '2022')
car.info()
to = Toyota('tundra', '2000')
to.info()

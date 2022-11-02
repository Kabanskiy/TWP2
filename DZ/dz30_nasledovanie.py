class Animals:
    def __init__(self, vid, otryad):
        self.vid = vid
        self.otryad = otryad
        self.dich = ' дикий'
        self.predator = 'медведь'

    def mlecopitaushie(self):
        print('Животное ' + self.vid + ' - ' + self.otryad)
    def zoo(self):
        print(self.vid + self.dich)
    def vseyadn(self):
        print('А животное ' + self.predator + ' - хищник')
        print(self.predator + ' тоже ' + self.dich)
# В класс из предыдущего урока добавьте три класса-наследника на ваше усмотрение.

class Slon(Animals):
    def __init__(self, vid, otryad):
        super().__init__(vid, otryad)
    def Biv(self):
        print('Бивни белые')
class Tiger(Animals):
    def __init__(self, vid, otryad):
        super().__init__(vid, otryad)
    def Meet(self):
        print('Ест мясо')
class Feesh(Animals):
    def __init__(self, vid, otryad):
        super().__init__(vid, otryad)
    def Ikra(self):
        print('Метает икру')

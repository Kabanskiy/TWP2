# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.

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

zver = Animals('заяц', "травоядное")
zver.mlecopitaushie()
zver.zoo()
zver.vseyadn()
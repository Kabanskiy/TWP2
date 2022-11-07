# Добавить абстрактный класс Animal и переопределить в нём все будущие абстрактные методы.
from abc import abstractmethod
class Animals:
    def __init__(self):
        pass
    @abstractmethod
    def _mlecopitaushie(self):
        pass
    @abstractmethod
    def zoo(self):
        pass

class Bear(Animals):
    def __init__(self):
        super().__init__()
        pass
    def _mlecopitaushie(self):
        print('Медведь')
    def zoo(self):
        print('Дикий зверь')

zver = Bear()
zver._mlecopitaushie()
zver.zoo()
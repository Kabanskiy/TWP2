from abc import abstractmethod  # в первую очередь импортируем из библиотеки abc метод абстракции

class Bytovaya_tehnika:
    def __init__(self):
        pass
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def zhiraf(self):
        pass
    @abstractmethod
    def closed(self):
        pass

class Holodos(Bytovaya_tehnika):
    def __init__(self):
        pass
    def open(self):
        print('Открыть холодильник')
    def zhiraf(self):
        print('Засунуть туда жирафа')
    def closed(self):
        print('Закрыть холодильник')

do_it1 = Holodos()
do_it1.open()
do_it1.zhiraf()
do_it1.closed()
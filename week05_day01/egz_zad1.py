class Punkt:
    def __init__(self):
        self.x: float = 0
        self.y: float = 0


class Ksztalt2D:
    def obwod(self) -> float:
        raise NotImplemented  # rzucenie wyjatku

    def show(self):
        x = self.obwod()
        print(f'Obwód figury wynosi {x}')


class Kolo(Ksztalt2D):
    def __init__(self):
        self.Sr: Punkt = None
        self.r: float = 0
        

class Trojkat(Ksztalt2D):
    def __init__(self):
        self.A: Punkt = None
        self.B: Punkt = None
        self.C: Punkt = None



def test01():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()


if __name__ == '__main__':
    test01()


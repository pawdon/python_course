class Punkt:
    def __init__(self, x, y):
        self.x: float = x
        self.y: float = y

    # __str__ i __repr__ sluza do ladnego wyswietlania obiektow
    # jesli __str__ nie jest zaimplementowane, ale jest __repr__, to
    # __repr__ zadziala tez wtedy, kiedy normalnie zadzialaloby __str__
    # __str__ dziala np przy print(pojedyncza_wartosc) albo str(pojedyncza_wartosc)
    # __repr__ dziala np przy print(lista) albo str(lista)
    def __repr__(self):
        return f'({self.x}, {self.y})'


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
    def __init__(self, Ax: float, Ay: float, Bx: float, By: float, Cx: float, Cy: float):
        self.A: Punkt = Punkt(Ax, Ay)
        self.B: Punkt = Punkt(Bx, By)
        self.C: Punkt = Punkt(Cx, Cy)



def test01():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()
    t = Trojkat(1, 2, 3, 4, 5, 6)


if __name__ == '__main__':
    test01()


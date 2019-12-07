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
    """
    def __init__(self, Ax: float=0, Ay: float=0, Bx: float=2, By: float=-2, Cx: float=2, Cy: float=2):
        self.A: Punkt = Punkt(Ax, Ay)
        self.B: Punkt = Punkt(Bx, By)
        self.C: Punkt = Punkt(Cx, Cy)
    """
    def __init__(self, A: Punkt, B: Punkt, C: Punkt):
        self.A: Punkt = A
        self.B: Punkt = B
        self.C: Punkt = C

    def __repr__(self):
        # return f'A{self.A}, B{self.B}, C{self.C}'
        return ', '.join([f'{key}{val}' for key, val in self.__dict__.items()])


def test01():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()
    t = Trojkat(1, 2, 3, 4, 5, 6)
    print(t)
    t = Trojkat()
    print(t)


def test02():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()
    A = Punkt(1, 2)
    B = Punkt(3, 4)
    C = Punkt(5, 6)
    t = Trojkat(A, B, C)
    print(t)


if __name__ == '__main__':
    test02()


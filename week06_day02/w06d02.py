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

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Trojkat:
    def __init__(self, A: Punkt = None, B: Punkt = None, C: Punkt = None):
        self.A: Punkt = A
        self.B: Punkt = B
        self.C: Punkt = C

        if self.A is None:
            self.A = Punkt(0, 0)
        if self.B is None:
            self.B = Punkt(2, -2)
        if self.C is None:
            self.C = Punkt(2, 2)

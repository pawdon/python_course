from typing import Union

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
    # Sposob dziala, realizuje funkcjonalnosc dwoch konstruktorow (domyslny i z liczbami)
    def __init__(self, Ax: float=0, Ay: float=0, Bx: float=2, By: float=-2, Cx: float=2, Cy: float=2):
        self.A: Punkt = Punkt(Ax, Ay)
        self.B: Punkt = Punkt(Bx, By)
        self.C: Punkt = Punkt(Cx, Cy)
    """
    """
    TO JEST ŹLE! WARTOŚCI MUTABLE (MODYFIKOWALNE) NIE POWINNY BYĆ ARGUMENTAMI DOMYŚLNYMI
    def __init__(self, A: Punkt=Punkt(0,0), B: Punkt=Punkt(2,-2), C: Punkt=Punkt(2,2)):
    """
    """
    # Sposob dziala, realizuje funkcjonalnosc dwoch konstruktorow (domyslny i z punktami)
    def __init__(self, A: Punkt=None, B: Punkt=None, C: Punkt=None):
        self.A: Punkt = A
        self.B: Punkt = B
        self.C: Punkt = C

        if self.A is None:
            self.A = Punkt(0, 0)
        if self.B is None:
            self.B = Punkt(2,-2)
        if self.C is None:
            self.C = Punkt(2, 2)
    """

    """
    # Sposob dziala, realizuje funkcjonalnosc trzech konstruktorow (domyslny, z liczbami i z punktami)
    # Nie obsluguje sytuacji Trojkat(Ax=5, Ay=7, A=Punkt(13, 15))
    def __init__(self, Ax: float=0, Ay: float=0, Bx: float=2, By: float=-2, Cx: float=2, Cy: float=2,
                 A: Punkt=None, B: Punkt=None, C: Punkt=None):

        self.A: Punkt = Punkt(Ax, Ay)
        self.B: Punkt = Punkt(Bx, By)
        self.C: Punkt = Punkt(Cx, Cy)

        if A is not None:
            self.A = A
        if B is not None:
            self.B = B
        if C is not None:
            self.C = C
    """

    def __init__(self,
                 Ax: float=None, Ay: float=None,
                 Bx: float=None, By: float=None,
                 Cx: float=None, Cy: float=None,
                 A: Punkt=None, B: Punkt=None, C: Punkt=None):

        self.A: Punkt = None
        self.B: Punkt = None
        self.C: Punkt = None

        # pojedyncze _ przed nazwa to protected, podwojne to private
        self.__a: float = 0
        self.__b: float = 0
        self.__c: float = 0

        # are_numbers_given jest rowne True, jesli ktorakolwiek z liczb Ax...Cy zostala podana
        are_numbers_given = any([Ax is not None, Ay is not None,
                                 Bx is not None, By is not None,
                                 Cx is not None, Cy is not None])
        are_points_given = (A is not None) or (B is not None) or (C is not None)

        if not are_numbers_given and not are_points_given:
            self.A = Punkt(0, 0)
            self.B = Punkt(2, -2)
            self.C = Punkt(2, 2)
        elif are_numbers_given and not are_points_given:
            self.A = Punkt(Ax, Ay)
            self.B = Punkt(Bx, By)
            self.C = Punkt(Cx, Cy)
        elif not are_numbers_given and are_points_given:
            self.A = A
            self.B = B
            self.C = C
        else:  # are_numbers_given and are_points_given
            raise RuntimeError('Albo liczby albo punkty powinny byc zadane, ale nie liczby i punkty jednoczesnie')

        self.__boki()

    def __repr__(self):
        return f'A{self.A}, B{self.B}, C{self.C}'
        # return ', '.join([f'{key}{val}' for key, val in self.__dict__.items()])

    def __boki(self):
        self.__a = self.B.distance(self.C)
        self.__b = self.A.distance(self.C)
        self.__c = Punkt.distance(self.A, self.B)

    def get_bok_a(self):
        return self.__a

    def get_bok_b(self):
        return self.__b

    def get_bok_c(self):
        return self.__c

    def set_punkt_A(self, val: Punkt):
        self.A = val
        self.__boki()

    def set_punkt_B(self, val: Punkt):
        self.B = val
        self.__boki()

    def set_punkt_C(self, val: Punkt):
        self.C = val
        self.__boki()


class TrojkatPython(Ksztalt2D):
    def __init__(self, A: Punkt=None, B: Punkt=None, C: Punkt=None):
        self.A: Punkt = A
        self.B: Punkt = B
        self.C: Punkt = C

        if self.A is None:
            self.A = Punkt(0, 0)
        if self.B is None:
            self.B = Punkt(2, -2)
        if self.C is None:
            self.C = Punkt(2, 2)

    @classmethod
    def create_from_numbers(cls, Ax: float=0, Ay: float=0, Bx: float=2, By: float=-2, Cx: float=2, Cy: float=2):
        return cls(A=Punkt(Ax, Ay), B=Punkt(Bx, By), C=Punkt(Cx, Cy))

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
    t = Trojkat(A, B, Punkt(5, 6))
    print(t)
    t1 = Trojkat()
    print(t1)
    t2 = Trojkat()
    print(t2)
    t1.A.x = 17
    print(t1)
    print(t2)


def test03():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()
    t = Trojkat()
    print(t)
    t = Trojkat(1, 2, 3, 4, 5, 6)
    print(t)
    A = Punkt(11, 12)
    B = Punkt(13, 14)
    t = Trojkat(A=A, B=B, C=Punkt(15, 16))
    print(t)
    # t = Trojkat(Ax=5, Ay=7, A=Punkt(13, 15))  # RuntimeError: Albo liczby albo punkty powinny byc zadane, ale nie liczby i punkty jednoczesnie


def test04():
    print('START')
    a = Ksztalt2D()  # __new__(), __init__(), __postinit__()
    # a.obwod()
    t = TrojkatPython()
    print(t)
    t = TrojkatPython.create_from_numbers()
    print(t)
    t = TrojkatPython.create_from_numbers(1, 2, 3, 4, 5, 6)
    print(t)
    A = Punkt(11, 12)
    B = Punkt(13, 14)
    t = TrojkatPython(A, B, Punkt(15, 16))
    print(t)
    # t = Trojkat(Ax=5, Ay=7, A=Punkt(13, 15))  # Ru


def test05():
    t = Trojkat(2, 3, 4, 5, 5, 7)
    print(t)
    print(t.get_bok_a(), t.get_bok_b(), t.get_bok_c())
    t.set_punkt_C(Punkt(9, 17))
    print(t.get_bok_a(), t.get_bok_b(), t.get_bok_c())


def program_8():
    t = Trojkat()
    print(t.get_bok_a(), t.get_bok_b(), t.get_bok_c())
    t.set_punkt_A(Punkt(-1, 0.3))
    t.set_punkt_B(Punkt(-1, 2.3))
    t.set_punkt_C(Punkt(3, 1.3))
    print(t.get_bok_a(), t.get_bok_b(), t.get_bok_c())


if __name__ == '__main__':
    program_8()


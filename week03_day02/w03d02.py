from dataclasses import dataclass
from enum import Enum


# dataclass implements eg. __init__, __eq__
@dataclass
class Vector2D_dataclass:
    # te pola wskoczyly na miejsce, gdzie wczesniej byly pola statyczne
    x: float
    y: float = 0

    def __post_init__(self):
        # wywolywane po __init__
        self.dist = self.abs()

    def __str__(self):
        return f'V({self.x}, {self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'V({self.x}, {self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # operator == overload
    # jesli mam object1 operator object2, to powoduje to wywolanie odpowieniej metody
    # na object1 przekazujac object2 jako argument
    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y
        # getattr(self, k) <==> self.__dict__.get(k) <~=> self.__dict__[k]
        self_keys = self.__dict__.keys()
        other_keys = other.__dict__.keys()
        if self_keys == other_keys:
            return all([getattr(self, k) == getattr(other, k) for k in self_keys])
        else:
            return False

    def __add__(self, other):
        # isinstance wspiera dziedziczenie
        # czyli sprawdza, czy other jest obiektem klasy Vector2D albo pochodnej
        if isinstance(other, Vector2D):
            x = self.x + other.x
            y = self.y + other.y
        elif isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other
        elif (isinstance(other, list) or isinstance(other, tuple)) and len(other) == 2:
            x = self.x + other[0]
            y = self.y + other[1]
        else:
            raise ValueError(f'Cannot add {self} and {other}')
        return self.__class__(x, y)  # <==> Vector2d(x, y)


def test_vector():
    v1 = Vector2D(3, 4)
    print(v1)
    print(v1.abs())
    v2 = Vector2D(3, 4)
    print(v1 == v2)
    v3 = v1 + v2
    print(v1, v2, v3)
    v4 = v1 + 5
    print(v4)
    v5 = v1 + [5, 6]
    print(v5)
    v6 = v1 + (5, 6)
    print(v6)


class Building:
    # klasa opisuje budowe czegos, wiec mozna sie dostac do czesci skladowych
    class Floor:
        def __init__(self):
            self.is_ground = False
            self.rooms_number = 0

    def __init__(self):
        # metoda opisuje zachowanie, wiec nie da sie dostac do czegos wewnatrz zachowania
        class ABC:
            pass
        xyz = 6
        self.floors = [Building.Floor(), self.Floor()]
        self.wall_color = 'white'


def test_building():
    build = Building()
    floor = Building.Floor()


# jesli nie chce podawac wartosci
class OtherEnum(Enum):
    NAME01 = object()  # musi miec jakas wartosc
    NAME02 = object()
    NAME03 = object()


class Color(Enum):
    RED = '#FF0000'
    GREEN = '#00FF00'
    BLUE = '#0000FF'


def test_enum():
    print(OtherEnum.NAME01.value)
    c1 = Color.RED
    print(c1.value, c1.name)
    print(c1)
    c2 = Color('#FF0000')
    print(c2)
    c3 = Color['RED']
    print(c3)
    print(c1 == c2, c2 == c3)
    for x in Color:
        print(x)

    print(len(Color))


if __name__ == '__main__':
    test_enum()

from dataclasses import dataclass


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


if __name__ == '__main__':
    test_vector()

from dataclasses import dataclass


@dataclass
class Vector2D:
    # te pola wskoczyly na miejsce, gdzie wczesniej byly pola statyczne
    x: float
    y: float = 0

    def __post_init__(self):
        # wywolywane po __init__
        print('Post init')

    def __str__(self):
        return f'V({self.x}, {self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


def test_vector():
    v1 = Vector2D(3, 4)
    print(v1)
    print(v1.abs())


if __name__ == '__main__':
    test_vector()

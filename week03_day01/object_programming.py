class MyClass:
    def __init__(self):
        print('haha')
        self.x = 0


class Person:
    def __init__(self, first_name, last_name, age=20):
        # self jest obiektem, na ktorym zostala wywolana metoda
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self, other_name):
        print(f'Hello {other_name}. My name is {self.first_name} {self.last_name}')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.age})'


def class_testing():
    # print(MyClass)
    # my_object = MyClass()  # tu wywoluje sie __init__
    # print(my_object)

    person = Person('Jan', last_name='Kowalski')  # tworzony jest obiekt i na nim zawolana jest metoda __init__
    print(person.first_name, person.last_name, person.age)
    person.say_hello('Anna')
    # <==>
    Person.say_hello(self=person, other_name='Anna')
    print(person)
    print(str(person))


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # wywolywane niejawnie podczas str(p1), a funkcja str jest wywolywana niejawnie w print
        return f'P({self.x}, {self.y})'

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Point3D(Point2D):
    def __init__(self, x, y, z):
        # super() pozwala na odniesienie sie do klasy bazowej
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        # wywolywane niejawnie podczas str(p1), a funkcja str jest wywolywana niejawnie w print
        return f'P({self.x}, {self.y}, {self.z})'


def test_point():
    p1 = Point2D(3, 4)
    p1.x = 7
    print(p1)  # P(7, 4)

    p2 = Point2D(10, 8)
    distance = p1.distance_to(p2)
    print(distance)  # 5
    print()

    p3 = Point3D(3, 4, 5)
    print(p3)

    print(p3.distance_to(p2))  # policzy dystans w 2D


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def field(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class RectangleInSpace:
    def __init__(self, top_left=None, dimensions=None):
        # left top corner
        self.top_left: Point2D = top_left
        self.dimensions: Rectangle = dimensions

    def get_extreme(self):
        left = self.top_left.x
        top = self.top_left.y
        right = self.top_left.x + self.dimensions.a
        bottom = self.top_left.y + self.dimensions.b
        return left, right, top, bottom

    def intersection1D(self, p1_start, p1_stop, p2_start, p2_stop):
        start = max(p1_start, p2_start)
        stop = min(p1_stop, p2_stop)
        return start, stop

    def intersection(self, other):
        self_left, self_right, self_top, self_bottom = self.get_extreme()
        other_left, other_right, other_top, other_bottom = other.get_extreme()

        left, right = self.intersection1D(self_left, self_right, other_left, other_right)
        top, bottom = self.intersection1D(self_top, self_bottom, other_top, other_bottom)

        width = right - left
        height = bottom - top
        if width < 0 or height < 0:
            return 0
        else:
            return Rectangle(width, height).field()

    def union(self, other):
        return self.dimensions.field() + other.dimensions.field() - self.intersection(other)

    def intersection_over_union(self, other):
        return self.intersection(other) / self.union(other)


def test_rect():
    r1 = Rectangle(a=7, b=5)
    print(r1.field())  # 35
    print(r1.perimeter())  # 24


def test_inters_over_union():
    r1 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    r2 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    print(r1.intersection_over_union(r2))  # 1.0

    r1 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    r2 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 10))
    print(r1.intersection_over_union(r2))  # 0.5

    r1 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(8, 5))
    r2 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    print(r1.intersection_over_union(r2))  # 0.5

    r1 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    r2 = RectangleInSpace(top_left=Point2D(4, 4), dimensions=Rectangle(4, 5))
    print(r1.intersection_over_union(r2))  # 0.6

    r1 = RectangleInSpace(top_left=Point2D(3, 4), dimensions=Rectangle(4, 5))
    r2 = RectangleInSpace(top_left=Point2D(9, 4), dimensions=Rectangle(4, 5))
    print(r1.intersection_over_union(r2))  # 0.0

    r1 = RectangleInSpace(top_left=Point2D(0, 0), dimensions=Rectangle(10, 20))
    r2 = RectangleInSpace(top_left=Point2D(5, 5), dimensions=Rectangle(5, 20))
    print(r1.intersection_over_union(r2))  # 0.3333333

    r1 = RectangleInSpace(top_left=Point2D(0, 0), dimensions=Rectangle(100, 100))
    r2 = RectangleInSpace(top_left=Point2D(50, 50), dimensions=Rectangle(10, 10))
    print(r1.intersection_over_union(r2))  # 0.01


if __name__ == '__main__':
    test_inters_over_union()

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


if __name__ == '__main__':
    test_inters_over_union()

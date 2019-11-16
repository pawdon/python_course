class MyClass:
    def __init__(self):
        print('haha')
        self.x = 0


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


class Person:
    number_of_people = 0
    my_list = []

    def __init__(self, first_name, last_name, age=20):
        # self jest obiektem, na ktorym zostala wywolana metoda
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__class__.number_of_people += 1  # OK
        # self.number_of_people += 1  # NOT OK
        # Person.number_of_people += 1  # OK

    def say_hello(self, other_name):
        print(f'Hello {other_name}. My name is {self.first_name} {self.last_name}')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.age})'

    @staticmethod
    def say_buu(repeat=1):
        print('Buu' * repeat)


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

    Person.say_buu(2)
    person.say_buu(3)

    person2 = Person('Anna', 'Nowak', 22)
    print('Number of people')
    print(Person.number_of_people)
    print(person2.number_of_people)
    print()

    Person.number_of_people = 10
    print(Person.number_of_people)
    print(person2.number_of_people)
    print()

    # operacja = przerywa referencje
    person2.number_of_people = 20
    print(Person.number_of_people)
    print(person2.number_of_people)
    print()

    Person.my_list.append('haha')
    print(Person.my_list)
    print(person2.my_list)
    print()

    person2.my_list.append('buu')
    print(Person.my_list)
    print(person2.my_list)
    print()

    person2.my_list = ['xx']
    print(Person.my_list)
    print(person2.my_list)
    print()


class ABC:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def say_hello(name):
        print('Hello', name)

    @staticmethod
    def say_buu():
        print('Buu')

    def say_hihi(self):
        print('Hihi', self.name)


@staticmethod
def say_buu2():
    print('Buu2')


def say_hihi2(self):
    print('Hihi2', self.name)



def test_abc():
    obj_abc = ABC('DEF')
    print(ABC.say_buu)
    print(obj_abc.say_buu)
    ABC.say_buu()  # Buu
    obj_abc.say_buu()  # Buu

    ABC.say_buu = say_buu2
    ABC.say_buu()  # Buu2
    obj_abc.say_buu()  # Buu2

    print(ABC.say_hihi)
    print(obj_abc.say_hihi)
    ABC.say_hihi(obj_abc)  # Hihi DEF
    obj_abc.say_hihi()  # Hihi DEF

    obj_abc.say_hihi = say_hihi2
    ABC.say_hihi(obj_abc)  # Hihi DEF
    obj_abc.say_hihi(obj_abc)  # Hihi2 DEF

    obj_abc.sth_else = 'Hi'
    print(obj_abc.sth_else)


class Car:
    def __init__(self, model, color, doors_number=5):
        self.model = model
        self.color = color
        self.doors_number = doors_number

    def start_engine(self):
        print('Brrrum')


def test_car():
    corsa = Car(model='Opel', color='silver')
    print(corsa.__dict__)  # tylko pola; nazwy i wartosci; zwykly slownik
    print(dir(corsa))  # pola i metody; lista nazw
    corsa.__dict__['model'] = 'Skoda'
    print(corsa.model)
    setattr(corsa, 'model', 'Volvo')
    print(corsa.model)
    print(getattr(corsa, 'model', 'Opel'))  # Opel is default
    print(getattr(corsa, 'has_radio', True))  # True is default

    print(Car)
    print(corsa)
    print(corsa.__class__)

    golf = corsa.__class__(model='VW', color='red')  # konstruktor
    # corsa.__class__ <==> Car
    print(corsa, corsa.model)
    print(golf, golf.model)


class XYZ:
    def __init__(self):
        self.name = 'X'

    def copy(self):
        # return XYZ()
        return self.__class__()


class XYZ2(XYZ):
    def __init__(self):
        super().__init__()
        self.name = 'Y'


def test_xyz():
    obj = XYZ2()
    obj_copy = obj.copy()
    print(obj_copy.name)


class ProcessSimpleBad:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def step1a(data):
        return data + '_A'

    @staticmethod
    def step1b(data):
        return data + '_B'

    @staticmethod
    def step1(data):
        data = ProcessSimpleBad.step1a(data)
        data = ProcessSimpleBad.step1b(data)
        return data

    @staticmethod
    def step2(data):
        return data + '_C'

    @staticmethod
    def pipeline(data):
        data = ProcessSimpleBad.step1(data)
        data = ProcessSimpleBad.step2(data)
        return data

    def process(self):
        return ProcessSimpleBad.pipeline(self.name)


class ProcessSimpleGood:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def step1a(data):
        return data + '_A'

    @staticmethod
    def step1b(data):
        return data + '_B'

    @classmethod
    def step1(cls, data):
        data = cls.step1a(data)
        data = cls.step1b(data)
        return data

    @staticmethod
    def step2(data):
        return data + '_C'

    @classmethod
    def pipeline(cls, data):
        data = cls.step1(data)
        data = cls.step2(data)
        return data

    def process(self):
        return self.pipeline(self.name)


class ProcessAdvanced(ProcessSimpleGood):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def step1b(data):
        return data + '_BXXX'


def test_process():
    pr = ProcessAdvanced('Jan')
    print(pr.process())

    print(ProcessSimpleGood.step1('buu'))


class MyAccessExample:
    def __init__(self):
        self.a = 1  # public
        self._b = 2  # protected
        self.c_ = 3  # public
        self._d_ = 4  # protected
        self.__e = 5  # private
        self.f__ = 6  # public
        self.__g__ = 7  # public

    def __str__(self):
        values = [self.a, self._b, self.c_, self._d_, self.__e, self.f__, self.__g__]
        return ','.join([str(x) for x in values])

    @property
    def property_e(self):
        print('GETTER')
        return self.__e

    @property_e.setter
    def property_e(self, value):
        print('SETTER')
        self.__e = value


def test_access():
    obj = MyAccessExample()
    print(obj)
    print(obj.__dict__)

    values = [obj.a, obj._b, obj.c_, obj._d_, obj._MyAccessExample__e, obj.f__, obj.__g__]
    print(','.join([str(x) for x in values]))

    print()
    x = obj.property_e
    print(x)
    obj.property_e = 17
    print(obj.__dict__)


if __name__ == '__main__':
    test_access()

def double_x(x):
    return 2 * x


def triple_x(x):
    return 3 * x


def modify_x(x, func):
    result = func(x)
    return result


def quadratic_equation(a, b, c):
    def delta(a, b, c):
        return b ** 2 - 4 * a * c

    x1 = (-b + delta(a, b, c) ** 0.5) / 2
    x2 = (-b - delta(a, b, c) ** 0.5) / 2

    return x1, x2


def test01():
    result = modify_x(7, double_x)
    print(result)
    result = modify_x(7, triple_x)
    print(result)

    print(quadratic_equation(1, 0, -9))

    modify_x_copy = modify_x
    result = modify_x_copy(8, triple_x)
    print(result)

    # skladnia lambdy
    # lambda moze byc tylko jednolinijkowa
    # lambda <lista argumentow rozdzielana przecinkami>: <rezultat>
    result = modify_x_copy(8, lambda x: 4 * x)
    print(result)


def test_lambda():
    func01 = lambda: print('haha')
    func01()

    func02 = lambda: ['red', 'green']
    result = func02()
    print(result)

    func03 = lambda x, y: x + y
    print(func03(4, 5))

    func04 = lambda x=9, y=1: x + y
    print(func04(y=4))

    data = [{'name': 'Jan', 'age': 15},
            {'name': 'Adam', 'age': 54},
            {'name': 'Agnieszka', 'age': 21}]
    print(data)
    # w sortowaniu key jest funkcja, ktora przyjmuje jako argument pojedynczy element list
    # i zwraca po czym sortowac
    # sort edytuje wewnetrznie liste
    data.sort(key=lambda x: x['name'])
    print(data)
    # sorted tworzy kopie
    print(sorted(data, key=lambda x: x['age']))


def choose_function(name):
    options = {'double': double_x, 'triple': triple_x}
    return options.get(name, lambda x: 4 * x)


def test_choose_function():
    result = choose_function('double')(7)
    print(result)

    result = choose_function('triple')(7)
    print(result)

    result = choose_function('xyz')(7)
    print(result)


class ABC:
    def __init__(self, name):
        self.name = name

    def __call__(self, other):
        return f'Hi {other}! I am {self.name}'


def test_func_obj():
    print(choose_function)
    print(dir(choose_function))
    print(choose_function.__class__)

    x = ABC('Jan')
    result = x('Tomek')
    print(result)

    choose_function.gy = 7
    print(choose_function.gy)


if __name__ == '__main__':
    test_func_obj()

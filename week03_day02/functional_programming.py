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
    pass


if __name__ == '__main__':
    test01()

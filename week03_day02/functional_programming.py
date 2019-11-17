def double_x(x):
    return 2 * x


def triple_x(x):
    return 3 * x


def modify_x(x, func):
    result = func(x)
    return result


def test01():
    result = modify_x(7, double_x)
    print(result)
    result = modify_x(7, triple_x)
    print(result)


if __name__ == '__main__':
    test01()

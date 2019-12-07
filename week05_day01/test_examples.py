def multiply(x, y):
    """

    :param x:
    :param y:
    :return:

    >>> multiply(2, 3)
    6
    """
    result = x * y
    print(f'{x} * {y} = {result}')
    return result


def silnia(n: int) -> int:
    """
    To jest funkcja licząca silnię z liczby naturalnej
    :param n: jakaś liczba naturalna
    :return: wynik silni

    >>> silnia(0)
    1
    >>> silnia(1)
    1
    >>> silnia(2)
    2
    >>> silnia(3)
    6
    """
    if n < 0:
        raise ValueError('n should be >= 0')
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

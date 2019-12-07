import pytest


def multiply(x, y):
    """

    :param x:
    :param y:
    :return:

    >>> multiply(2, 3)
    2 * 3 = 6
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
    >>> silnia(-1)
    Traceback (most recent call last):
        ...
    ValueError: n should be >= 0
    """
    if n < 0:
        raise ValueError('n should be >= 0')
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def test_01():
    assert 1 == 1
    assert 2 == 2, 'Opcjonalny opis'


# @pytest.mark.parametrize przyjmuje 2 argumenty:
# stringa z nazwami argumentow rozdzielanymi przecinkami
# liste tupli z wartosciami
@pytest.mark.parametrize('arg, val', [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24)])
def test_silnia_correct(arg, val):
    assert silnia(arg) == val


def test_silnia_incorrect():
    # match jest opcjonalne
    with pytest.raises(ValueError, match='n should be >= 0'):
        silnia(-1)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    pass

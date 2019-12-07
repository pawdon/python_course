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


def more_values_to_test(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            split = line.strip().split(',')
            val = int(split[0]), int(split[1])
            values.append(val)
    return values


# @pytest.mark.parametrize przyjmuje 2 argumenty:
# stringa z nazwami argumentow rozdzielanymi przecinkami
# liste tupli z wartosciami
@pytest.mark.parametrize('arg, val', [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24)] + more_values_to_test('test_silnia_values.csv'))
def test_silnia_correct(arg, val):
    assert silnia(arg) == val


def test_silnia_incorrect():
    # match jest opcjonalne
    with pytest.raises(ValueError, match='n should be >= 0'):
        silnia(-1)


# fixture sluzy do przygotowania danych do testow
@pytest.fixture(scope='session', params=['Volvo', 'Skoda', 'Audi'])
def prepare_data(request):
    # jakies laczenie sie z baza danych itp
    # generalnie duze przygotowanie obiektu
    print('\nSTART_PREPARE_DATA')
    yield request.param
    print('\nSTOP_PREPARE_DATA')


def test_prepared_data(prepare_data):
    assert prepare_data in ['Volvo', 'Skoda', 'BMW', 'Toyota', 'Audi']


def test_prepared_data2(prepare_data):
    assert len(prepare_data) < 100


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    pass

def divide(x, y):
    """
    Jesli dzielenie przez 0, to zwroc None
    """
    print(f'\nDzielimy {x} przez {y}')
    try:
        val = x / y
    except ZeroDivisionError as e:
        print(f'Dzielenie przez 0. Komunikat = {e}')
        val = None
    except TypeError:
        print(f'Jeden z argumentow nie jest liczba')
        val = None
    else:
        print('Wszystko OK')
    finally:
        print('Uff, koniec')
    return val


def divide2(x, y):
    """
    Jesli dzielenie przez 0, to zwroc None
    """
    print(f'\nDzielimy {x} przez {y} drugim sposobem')
    try:
        val = x / y
    except Exception as e:
        print(f'Blad. Komunikat = {e}')
        val = None
        # tu wykona sie finally
        return None
    else:
        print('Wszystko OK')
    finally:
        print('Uff, koniec')
    return val


def divide3(x, y):
    if y == 0:
        raise ValueError('PAMIETAJ SKNERO, NIE DZIEL PRZEZ ZERO')
    return x / y


if __name__ == '__main__':
    print(divide(6, 2))
    print(divide(4, 0))
    print(divide(None, 0))

    print(divide2(6, 2))
    print(divide2(4, 0))
    print(divide2(None, 0))

    print(divide3(2, 0))

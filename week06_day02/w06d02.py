def test01():
    my_list = [1, 2, 3]
    my_number = 3

    func1 = lambda a_number: [i * a_number for i in my_list]
    func2 = lambda a_list: [my_number * i for i in a_list]

    print(func1(4))
    print(func2([3, 4]))

    return func1, func2


def test02():
    my_list = [11, 12, 13]
    my_number = 13
    func1, func2 = test01()
    print(func1(4))
    print(func2([3, 4]))


class Obywatel:
    class AdresZameldowania:
        def __init__(self, kod_pocztowy, miejscowosc, ulica, numer_domu, numer_mieszkania):
            self.kod_pocztowy = kod_pocztowy
            self.miejscowosc = miejscowosc
            self.ulica = ulica
            self.numer_domu = numer_domu
            self.numer_mieszkania = numer_mieszkania

        def __repr__(self):
            return f'{self.kod_pocztowy} {self.miejscowosc}, {self.ulica} {self.numer_domu}/{self.numer_mieszkania}'

    def __init__(self, imie, nazwisko, adres_zameldowania):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_zameldowania = adres_zameldowania

    def __repr__(self):
        return f'{self.imie} {self.nazwisko} zameldowany w {self.adres_zameldowania}'


def test_obywatel():
    jan = Obywatel('Jan', 'Kowalski', Obywatel.AdresZameldowania('31-044', 'Kraków', 'Grodzka', 50, 1))
    print(jan)


if __name__ == '__main__':
    test_obywatel()


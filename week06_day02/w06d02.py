import random


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


class Walka:
    def __init__(self, atakujacy, broniacy):
        self.atakujacy: Postac = atakujacy
        self.broniacy: Postac = broniacy
        self.ataki = []

    def przeprowadz_walke(self):
        numer_ataku = 0
        atak = Atak(self.atakujacy, self.broniacy, numer_ataku)
        while atak.atakujacy.czy_atakuje(atak):
            self.ataki.append(atak)
            atak.przeprowadz_atak()

            numer_ataku += 1
            atak = Atak(atak.broniacy, atak.atakujacy, numer_ataku)


class Atak:
    def __init__(self, atakujacy, broniacy, numer_ataku_w_walce):
        self.atakujacy: Postac = atakujacy
        self.broniacy: Postac = broniacy
        self.numer_ataku_w_walce: int = numer_ataku_w_walce

        self.punkty_ataku = 0
        self.unikniecie = False
        self.punkty_obrony = 0
        self.obrazenia = 0

    def __repr__(self):
        info = f'{self.atakujacy.imie} {self.numer_ataku_w_walce * "kontr"}atakuje ({self.punkty_ataku}). '
        if self.unikniecie:
            info += f'{self.broniacy.imie} unika ataku. '
        else:
            info += f'{self.broniacy.imie} broni sie ({self.punkty_obrony}) i otrzymuje obrazenia {self.obrazenia}. '
        info += f'Stan po ataku: {self.atakujacy}, {self.broniacy}'
        return info

    def przeprowadz_atak(self):
        self.punkty_ataku = self.atakujacy.punkty_ataku(self)
        self.unikniecie = self.broniacy.czy_udalo_sie_uniknac(self)
        if not self.unikniecie:
            self.punkty_obrony = self.broniacy.punkty_obrony(self)
            mozliwe_obrazenia = max(self.punkty_ataku - self.punkty_obrony, 0)
            self.obrazenia = min(self.broniacy.zycie, mozliwe_obrazenia)

        self.broniacy.reakcja_na_otrzymany_atak(self)
        self.atakujacy.reakcja_na_zadany_atak(self)
        print(self)


class Postac:
    def __init__(self, imie, zycie, sila, wytrzymalosc=0, zrecznosc=0, szansa_na_krytyczne=0, szansa_na_kontratak=0):
        self.imie = imie
        self.zycie = zycie
        self.sila = sila
        self.wytrzymalosc = wytrzymalosc
        self.zrecznosc = zrecznosc
        self.szansa_na_krytyczne = szansa_na_krytyczne
        self.szansa_na_kontratak = szansa_na_kontratak

        assert 0 <= self.zrecznosc <= 1
        assert 0 <= self.szansa_na_krytyczne <= 1

    def __repr__(self):
        return f'{self.imie} ({self.zycie})'

    def uwzglednij_trafienie_krytyczne(self, wartosc):
        if self.szansa_na_krytyczne > random.random():
            wartosc *= 2
        return wartosc

    def punkty_ataku(self, informacja_o_ataku: Atak):
        wartosc = self.sila
        return self.uwzglednij_trafienie_krytyczne(wartosc)

    def punkty_obrony(self, informacja_o_ataku: Atak):
        return self.wytrzymalosc

    def czy_udalo_sie_uniknac(self, informacja_o_ataku: Atak):
        return self.zrecznosc > random.random()

    def czy_atakuje(self, informacja_o_potencjalnym_ataku: Atak):
        decyzja = False
        if informacja_o_potencjalnym_ataku.numer_ataku_w_walce == 0:
            decyzja = True
        elif informacja_o_potencjalnym_ataku.numer_ataku_w_walce == 1:
            decyzja = self.szansa_na_kontratak > random.random()
        else:
            decyzja = False
        return decyzja

    def reakcja_na_zadany_atak(self, informacja_o_ataku: Atak):
        pass

    def reakcja_na_otrzymany_atak(self, informacja_o_ataku: Atak):
        self.zycie -= informacja_o_ataku.obrazenia


def testuj_gre():
    rycerz = Postac('Rycerz', zycie=100, sila=10, wytrzymalosc=2, szansa_na_kontratak=1)
    smok = Postac('Smok', zycie=200, sila=20, wytrzymalosc=5, szansa_na_kontratak=1, zrecznosc=1)
    Walka(rycerz, smok).przeprowadz_walke()



if __name__ == '__main__':
    testuj_gre()


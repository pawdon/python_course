from typing import Sequence, List, Dict
from week02_day01.w03d01 import mean_sdv


def write_to_file_stupid_way():
    # NIGDY TAK NIE ROBCIE
    f = open('test_file.txt', 'w')
    f.write('Jan Kowalski')
    f.close()


def write_to_file(filename='test_file.txt'):
    with open(filename, 'w') as f:
        f.write('Jan Kowalski\n')
        f.write('Kamil Nowak\n')
        f.write('Adam Malysz\n')


def read_from_file(filename='test_file.txt'):
    with open(filename, 'r') as f:
        # nawet jesli plik nie istnieje albo wystapil inny problem,
        # to po wyjsciu z bloku with, plik bedzie poprawnie zamkniety
        print('\nfull')
        print(f.read())
        print(f.read())  # tu juz nic nie ma

    with open(filename, 'r') as f:
        print('\nreadline')
        print(f.readline(), end='')
        print(f.readline(), end='')

    with open(filename, 'r') as f:
        print('\ncorrect way')
        for line in f:  # iterate over lines
            print(line, end='')


def my_print(*args, begin='', end='\n'):
    print(begin, end='')
    print(*args, end=end)


def simple_tests():
    write_to_file()
    read_from_file('test_file.txt')
    print()
    my_print('Ala', 'ma', 'kota', end=' haha\n', begin='moja funkcja: ')


def cars_models_to_file(*models, filename):
    with open(filename, 'w') as f:
        for m in models:
            f.write(f'{m}\n')


def cars_from_file(filename):
    with open(filename, 'r') as f:
        return [m.strip() for m in f]


"""
przeczytaj plik po linii
podziel na poszczegolne wartosci
wypisz

'Name,Sex,Age,Height,Weight,Team,Medal'.split(',')
['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'Medal']
','.join(['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'Medal'])
'Name,Sex,Age,Height,Weight,Team,Medal'
"""
def read_csv(filename) -> List[Dict]:
    data = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            data.append({k: v for k, v in zip(keys, values)})
    return data


def read_csv2(filename):
    full_list = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            single_dict = {k: v for k,v in zip(keys, values)}
            full_list.append(single_dict)
    return full_list


def print_medals(filename):
    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            # name, *_, medal = line.strip().split(',')
            # print(f'{name} got {medal.lower()} medal')
            values = line.strip().split(',')
            print(f'{values[0]} got {values[6].lower()} medal')


# Age -> int
# Height -> float
# Weight -> float
def type_data(data: List[Dict]):
    for d in data:
        d['Age'] = int(float(d['Age']))
        d['Height'] = float(d['Height'])
        d['Weight'] = float(d['Weight'])


if __name__ == '__main__':
    data: List[Dict] = read_csv('ski_jumping_2014_medals.csv')
    type_data(data)
    print(data)
    heights = [x['Height'] for x in data]
    print(heights)
    print(mean_sdv(heights))



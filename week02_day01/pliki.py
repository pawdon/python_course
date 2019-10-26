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
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    write_to_file()
    read_from_file('test_file.txt')

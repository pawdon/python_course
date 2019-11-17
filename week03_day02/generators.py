def test_range():
    a = range(10)
    print(a)
    print(list(a))


def my_generator():
    with open('box_since_2000.csv', 'r') as file:
        keys = file.readline()
        for line in file:
            print(line)


def test_my_generator():
    my_generator()


if __name__ == '__main__':
    test_my_generator()

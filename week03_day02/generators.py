def test_range():
    a = range(10)
    print(a)
    print(list(a))


def my_generator():
    with open('box_since_2000.csv', 'r') as file:
        keys = file.readline().strip().split(';')
        for line in file:
            values = line.strip().split(';')
            single_dict = {key: value for key, value in zip(keys, values)}
            print(single_dict)


def test_my_generator():
    my_generator()


if __name__ == '__main__':
    test_my_generator()

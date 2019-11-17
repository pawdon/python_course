def test_range():
    a = range(10)
    print(a)
    print(list(a))


def my_generator(filename):
    print('\tStart generator')
    with open(filename, 'r') as file:
        print('\tOpened file')
        keys = file.readline().strip().split(';')
        for i, line in enumerate(file):
            print(f'\tStart single line {i}')
            values = line.strip().split(';')
            single_dict = {key: value for key, value in zip(keys, values)}
            yield single_dict  # taki maly return
            print(f'\tEnd single line {i}')


def test_my_generator():
    results = my_generator(filename='box_since_2000.csv')  # jeszcze sie nic nie wykonalo
    print('\tStart for loop', type(results))
    for i, single_dict in enumerate(results):
        if i >= 10:
            break
        print(single_dict['Name'], single_dict['Height'], single_dict['Weight'])


if __name__ == '__main__':
    test_my_generator()

def test_range():
    a = range(10)
    print(a)
    print(list(a))


def my_generator(filename):
    results = []
    with open(filename, 'r') as file:
        keys = file.readline().strip().split(';')
        for line in file:
            values = line.strip().split(';')
            single_dict = {key: value for key, value in zip(keys, values)}
            results.append(single_dict)
    return results


def test_my_generator():
    results = my_generator(filename='box_since_2000.csv')
    for single_dict in results:
        print(single_dict['Name'], single_dict['Height'], single_dict['Weight'])


if __name__ == '__main__':
    test_my_generator()

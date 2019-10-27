from typing import Sequence, List, Dict
import json
import yaml


def test01():
    names = ['Jan', 'Anna', 'Karol', 'Marcin', 'Dominik', 'Zuzanna']
    ages = [17, 25, 42, 65, 21, 33]
    heights = [173, 156, 184, 164, 191, 166]
    names_lower = [n.lower() for n in names]
    data = [{'name': n, 'age': a, 'height': h} for n, a, h in zip(names, ages, heights)]
    print(data)

    for d in data:
        d['name'] = d['name'].lower()
        d['age'] += 1

    print(data)

    data2 = [{'name': n.lower() + 'Kowalski',
              'age': a + 1,
              'height': h}
             for n, a, h in zip(names, ages, heights)]
    print(data2)


def read_csv(filename, sep=';') -> List[Dict]:
    data = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(sep)
        for line in f:
            values = line.strip().split(sep)
            data.append({k: v for k, v in zip(keys, values)})
    return data


def save_csv(data: List[Dict], filename, sep=';'):
    keys = data[0].keys()
    with open(filename, 'w') as f:
        header = sep.join(keys) + '\n'
        f.write(header)
        for d in data:
            values = [f'{d[key]}' for key in keys]
            row = sep.join(values) + '\n'
            f.write(row)


def filter_long(input_list: List[Dict], key, value) -> List[Dict]:
    new_list = []
    for data in input_list:
        if data[key] == value:
            new_list.append(data)
    return new_list


def filter(input_list: List[Dict], key, value) -> List[Dict]:
    return [data for data in input_list if data[key] == value]


# save_csv2([{'x': 5, 'y': 6}, {'y': 6, 'x': 5}], filename='test.csv')
def save_csv2(input_list: List[Dict], filename, sep=';'):
    with open(filename, 'w') as f:
        keys = input_list[0].keys()
        header = sep.join(keys) + '\n'
        f.write(header)
        for data in input_list:
            values = [str(data[key]) for key in keys]
            row = sep.join(values) + '\n'
            f.write(row)


def test_save_csv():
    # data: List[Dict] = read_csv(filename='athlete_events_since_2000.csv')
    # data = filter(data, key='Sport', value='Boxing')
    # save_csv(data, filename='box_since_2000.csv', sep=';')
    """
    ','.join(['Jan', 'Adam', 'Kowalski'])
    'Jan,Adam,Kowalski'
    """
    # print('START')
    # print(yaml.dump(data[0:100]))
    save_csv2([{'x': 5, 'y': 6}, {'y': 6, 'x': 5}], filename='test.csv')


def get_unique(input_list: List[Dict], key):
    values = [data[key] for data in input_list]
    return set(values)


def get_sorted_unique(input_list: List[Dict], key):
    unique_set = get_unique(input_list, key)
    unique_list = list(unique_set)
    sorted_unique_list = sorted(unique_list)
    return sorted_unique_list


def remove_column(input_list: List[Dict], key):
    for data in input_list:
        data.pop(key)


if __name__ == '__main__':
    data: List[Dict] = read_csv(filename='box_since_2000.csv', sep=';')
    remove_column(data, key='Sport')
    save_csv(data, filename='box_since_2000_simple.csv', sep=';')
    # teams = get_sorted_unique(data, key='Team')
    # print(len(teams), teams)

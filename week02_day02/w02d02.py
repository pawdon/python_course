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


def read_csv(filename, c=';') -> List[Dict]:
    data = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(c)
        for line in f:
            values = line.strip().split(c)
            data.append({k: v for k, v in zip(keys, values)})
    return data


if __name__ == '__main__':
    data = read_csv(filename='athlete_events_since_2000.csv')
    data = choose_sport(data, name='Boxing')
    print('START')
    print(yaml.dump(data[0:100]))

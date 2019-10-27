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


def str2float(data: str):
    """
    if data != '':
        return float(data)
    else:
        return None
    """
    # return float(data) if data else None
    return float(data) if data != '' else None


def str2int(data: str):
    data_float = str2float(data)
    """
    if data_float is not None:
        return int(data_float)
    else:
        return None
    """
    # return int(data_float) if data_float else None
    return int(data_float) if data_float is not None else None


def type_data(data: List[Dict]):
    for d in data:
        d['ID'] = str2int(d['ID'])
        d['Age'] = str2int(d['Age'])
        d['Year'] = str2int(d['Year'])
        d['Height'] = str2float(d['Height'])
        d['Weight'] = str2float(d['Weight'])


# kluczem sa panstwa
# wartosciami sa listy slownikow odpowiadajace zawodnikom danego panstwa
def result_per_team(input_list: List[Dict], year):
    filtered_data = filter(input_list, key='Year', value=year)

    teams = get_sorted_unique(filtered_data, key='Team')
    result = {}
    for team in teams:
        result[team] = [data for data in filtered_data if data['Team'] == team]

    return result


def get_people_on_the_podium(input_list: List[Dict]):
    return [{'Medal': data['Medal'],
             'Name': data['Name']}
            for data in input_list if data['Medal'] != '']


def get_medals_per_team(results_per_team):
    medals_per_team = {}
    for team, result in results_per_team.items():
        people_on_the_podium = get_people_on_the_podium(result)
        medals = [x['Medal'] for x in people_on_the_podium]
        medals_per_team[team] = {'Podium': people_on_the_podium,
                                 'Score': medals_to_score(medals)}
    return medals_per_team


def medals_to_score(medals):
    multipliers = {'Bronze': 1, 'Silver': 3, 'Gold': 5}
    sub_scores = [multipliers.get(m, 0) for m in medals]
    return sum(sub_scores)


def sorting_key(element):
    return element['Score']


def sort_teams(medals_per_team):
    result = [{'Team': key, 'Score': value['Score'], 'Podium': value['Podium']}
              for key, value in medals_per_team.items()]
    result.sort(key=sorting_key, reverse=True)
    return result


def find_best_team(data: List[Dict], year):
    results_per_team = result_per_team(data, year=year)
    with open('results.yaml', 'w') as f:
        f.write(yaml.dump(results_per_team))

    """
    Bronze = 1 pkt
    Silver = 3 pkt
    Gold = 5 pkt
    """
    medals_per_team = get_medals_per_team(results_per_team)
    with open('medals.yaml', 'w') as f:
        f.write(yaml.dump(medals_per_team))

    sorted_teams = sort_teams(medals_per_team)
    with open('sorted_teams.yaml', 'w') as f:
        f.write(yaml.dump(sorted_teams))
        
    return sorted_teams[0]['Team']


if __name__ == '__main__':
    data: List[Dict] = read_csv(filename='box_since_2000_simple.csv', sep=';')
    type_data(data)
    find_best_team(data, year=2016)

    """
    1. Policz sredni wzrost mezczyzn z danego kraju
    2. To samo, tylko dla tych, ktorzy zdobyli jakis medal
    3. To samo dla wieku
    4. To samo, ale najpierw podzielcie na kategorie wagowe
    5. Znajdz minimalna i maksymalna wage w danej kategorii wagowej dla mezczyzn i kabiet
    """

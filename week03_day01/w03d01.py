from typing import Sequence, List, Dict


# multiply_by([2, 4, 5], 7) -> [14, 28, 35]
def multiply_by(my_list: Sequence, multiplier: float) -> List:
    """
    new_list = []
    for x in my_list:
        new_list.append(x * multiplier)
    return new_list
    """
    return [x * multiplier for x in my_list]


def name_people(first_names, last_names, ages):
    return [f'{first} {last}, age = {age}' for first, last, age in zip(first_names, last_names, ages)]


def name_people2(first_names, last_names, ages):
    return [{'name': f'{first} {last}', 'age': age} for first, last, age in zip(first_names, last_names, ages)]


def people_to_file(my_list: List[Dict], filename):
    """
    1,Jan,Kowalski,M,24
    2,Julia,Nowak,F,31
    3,Anna,Kolodziej,F,16
    """
    with open(filename, 'w') as f:
        for i, person in enumerate(my_list, 1):
            name = person['name']
            age = person['age']
            first_name, last_name = name.split(' ')
            sex = 'F' if first_name.endswith('a') else 'M'
            row = ','.join([str(i), first_name, last_name, sex, str(age)])
            f.write(row + '\n')


if __name__ == '__main__':
    result = name_people2(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kolodziej'], [24, 31, 16])
    people_to_file(result, 'people.csv')

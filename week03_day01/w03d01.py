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


if __name__ == '__main__':
    # result = multiply_by([2, 4, 5], 7)
    result = name_people2(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kolodziej'], [24, 31, 16])
    print(result)

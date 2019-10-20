from typing import List, Sequence, Dict
import itertools
# List implements Sequence
# list implements List and Sequence
# dict implements Sequence, but not List
# List[str]
# Dict[str, int]

models = ['Volvo', 'Toyota', 'BMW', 'Mitsubishi', 'Skoda', 'Ford']
colors = ['Red', 'Black', 'Silver', 'Blue']
doors_count = [2, 3, 4]


def get_engines_list(minimum, maximum, step=0.1):
    value = minimum
    engines_list = []
    while value <= maximum:
        engines_list.append(value)
        value = round(value + step, 1)
    return engines_list


engines = get_engines_list(minimum=1.0, maximum=2.3, step=0.2)  # [1.0, 1.2, ..., 2.2]


def print_models(models):
    for m in models:
        print(m)


def print_models_with_nr(models):
    for i, m in enumerate(models):
        print(f'{i}: {m}')


def print_model_color_unique(models: Sequence[str], colors: List[str]):
    for m, c in zip(models, colors):
        print(f'{m} is {c.lower()}')


def return_lower(text: str='Haha') -> str:
    return text.lower()


def test_type_annotation(first_name: str, last_name: str=None, age: int=18) -> str:
    text: str = 'haha'
    if last_name is None:
        last_name = 'Kowalski'
    return f'{first_name} {last_name} is {age} years old'


def print_every_pair_simple(models, colors):
    for m in models:
        for c in colors:
            print(f'{m} is {c.lower()}')


def print_every_pair(models, colors):
    for m, c in itertools.product(models, colors):
        print(f'{m} is {c.lower()}')


def get_model_color_unique(models, colors):
    my_list = []
    for m, c in zip(models, colors):
        my_dict = {'model': m, 'color': c.lower()}
        my_list.append(my_dict)
    return my_list


def my_dict(**x):
    return x


def get_model_color_unique2(models, colors):
    for m, c in zip(models, colors):
        diction = {'model': m, 'color': c.lower()}
        # <==>
        diction = dict(model=m, color=c)
        # <==>
        diction = my_dict(model=m, color=c)
        print(diction)


def get_models(list_of_dicts):
    my_list = []
    for d in list_of_dicts:
        model = d['model']  # raise Exception if 'model' is not a valid key of d
        # <~=>
        model = d.get('model')  # return None if 'model' is not a valid key of d
        my_list.append(model)
    return my_list


def get_models_ver2(list_of_dicts):
    return [d['model'] for d in list_of_dicts]


def get_models2(list_of_dicts):
    my_list = []
    for i, d in enumerate(list_of_dicts):
        new_d = {'id': i, 'model': d['model']}
        my_list.append(new_d)
    return my_list


def get_models2_ver2(list_of_dicts):
    return [{'id': i, 'model': d['model']} for i, d in enumerate(list_of_dicts)]


def valid_number(a=None):
    a = a if a is not None else [1, 2, 3]
    return a

def one_liners():
    print("IF")
    a = 10
    '''
    if a == 10:
        b = 3
    else:
        b = 8'''
    b = 3 if a == 10 else 8
    c = 3 if a == 11 else 8
    print(a, b, c)
    print(valid_number())
    print(valid_number(7))

    print("\nLIST 01")
    my_list = list(range(10, 40, 2))
    print(my_list)
    d = [2 * x for x in my_list]
    '''
    d = []
    for x in my_list:
        d.append(2 * x)'''
    print('d', d)

    my_list2 = ['Red', 'Blue', 'Green', 'Black', 'White']
    e = [f"{str(i).rjust(3, '0')}_{color}" for i, color in enumerate(my_list2, 5)]
    print(e)

    d2 = [2 * x for x in range(10, 40, 2)]
    print(d2)


def my_empty_fun(a, b):
    pass


if __name__ == '__main__':
    # print_models(models)
    # print_models_with_nr(models)  # 0: Volvo
    # print_model_color_unique(models, colors)  #  Volvo is red
    # print(test_type_annotation('Jan', age=25))
    # print_model_color_unique(models, colors)
    # get_model_color_unique2(models, colors)  # [{'model': 'Volvo', 'color': 'red'}, {{'model': 'Toyota', 'color': 'black'}]
    # x = get_model_color_unique(models, colors)
    # print(x)
    # y = get_models_ver2(x)  # ['Volvo', 'Toyota', 'BMW', 'Mitsubishi']
    # print(y)
    # y2 = get_models2_ver2(x)  # [{'id': 0, 'model': 'Volvo'}, {'id': 1, 'model': 'Toyota'}, {'id': 2, 'model': 'BMW'}, {'id': 3, 'model': 'Mitsubishi'}]
    # print(y2)
    one_liners()

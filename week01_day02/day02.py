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

    d3 = [x % 3 for x in range(10, 40, 2)]
    print(d3)

    d4 = [{'a': x, 'b': x // 3, 'c': x % 3} for x in range(10, 40, 2)]
    print(d4)

    d5 = ['podzielne' if x % 3 == 0 else "niepodzielne" for x in range(10)]
    print(d5)

    d6 = [x for x in range(10) if x % 3 == 0]
    print(d6)

    d7 = ['podzielne' if x % 3 == 0 else "niepodzielne" for x in range(10) if x % 3 == 0]
    print(d7)

    d8 = [x for x in range(100) if x % 5 == 0]
    print(d8)

    print("\nDICT 01")
    my_list2 = ['Red', 'Blue', 'Green', 'Black', 'White']
    my_dict1 = {color: i for i, color in enumerate(my_list2)}
    print(my_dict1)

    my_dict2 = {color: i * 2 for i, color in enumerate(my_list2) if i % 2 == 0}
    print(my_dict2)

    my_dict3 = {color: i if i % 2 == 0 else i * 10 for i, color in enumerate(my_list2)}
    print(my_dict3)

    my_dict4 = {color.lower() if i % 2 == 0 else color.upper(): i for i, color in enumerate(my_list2)}
    print(my_dict4)


def my_empty_fun(a, b):
    pass


def rect(a, b):
    return a * b


def check(fun, result, *args, **kwargs):
    if fun(*args, **kwargs) == result:
        print('OK')
    else:
        print('NOT OK')


def magic_stars_again2():
    my_list = [{'arguments': (2, 3), 'result': 6},
               {'arguments': (4, 5), 'result': 20},
               {'arguments': (7, 3), 'result': 42},
               {'arguments': (3, 3), 'result': 9}]

    for d in my_list:
        check(rect, d['result'], *d['arguments'])


def magic_stars_again():
    list_of_lists_or_tuples = [(2, 3), (4, 10), [7, 9]]
    for d in list_of_lists_or_tuples:
        p = rect(d[0], d[1])
        # <==>
        p = rect(*d)
        print(p)

    print()
    list_of_dicts = [{'a': 2, 'b': 3}, {'a': 4, 'b': 10}, dict(a=7, b=9)]
    for d in list_of_dicts:
        p = rect(a=d['a'], b=d['b'])
        # <==>
        p = rect(**d)
        print(p)

    print()
    my_list = [{'arguments': (2, 3), 'result': 6},
               {'arguments': (4, 5), 'result': 20},
               {'arguments': (7, 3), 'result': 42},
               {'arguments': (3, 3), 'result': 9}]

    for d in my_list:
        if rect(*d['arguments']) == d['result']:
            print('OK')
        else:
            print('NOT OK')


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
    # one_liners()
    # print(get_model_color_unique(models, colors))
    magic_stars_again2()

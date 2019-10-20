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

print('__name__', __name__)
if __name__ == '__main__':
    # print_models(models)
    # print_models_with_nr(models)  # 0: Volvo
    # print_model_color_unique(models, colors)  #  Volvo is red
    # print(test_type_annotation('Jan', age=25))
    print_every_pair(models, colors)

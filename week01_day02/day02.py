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


# print_models(models)
# print_models_with_nr(models)  # 0: Volvo
print_model_color_unique(models, colors)  #  Volvo is red

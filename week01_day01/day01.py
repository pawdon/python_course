def test01():
    print('Hello world')  # comment
    """
    Multi line comment
    """


def say_hello(first_name, last_name='Kowalski',
              age=18):
    print(f'Hi {first_name} {last_name}. You are {age} years old')
    # Najpierw wszystkie pozycyjne, potem wszystkie domyslne
    # Najpierw podaje pozycyjnie, potem podaje nazwane


def say_hello2(first_name, last_name):
    print('Hi', first_name, last_name)
    print('Hi' + str(first_name) + str(last_name))
    print(f'Hi {first_name} {last_name}')


def say_hello_test():
    say_hello('Pawel')
    # say_hello(5)
    # say_hello2('Jan', 'Kowalski')
    # say_hello('Jan', 'Nowak')
    # say_hello('Jan')
    # say_hello(first_name='Jan', age=22)
    # say_hello(first_name='Jan',
    #           age=22,
    #          last_name='Nowak')


def rect(a, b):
    pole = a * b
    obwod = 2 * a + 2 * b
    print('Pole =', pole)
    print('Obwod =', 2 * a + 2 * b)
    return pole, obwod


def rect_show():
    x = rect(2, 3)
    print(x)
    pole, obwod = rect(2, 3)
    print(pole)
    print(obwod)


def my_append(value, my_list=[1, 2]):
    my_list.append(value)
    return my_list


def my_append2(value, my_list=(1, 2)):
    my_list = list(my_list)
    my_list.append(value)
    return my_list


def my_append3(value, my_list=None):
    if my_list is None:
        my_list = [1, 2]
    my_list.append(value)
    return my_list


def my_append4(value, my_list):
    my_list.append(value)


def my_append5(value, my_list):
    my_list = [3, 4]
    my_list.append(value)


def show_my_append():
    print(my_append(2, [3, 4]))
    print(my_append(5))
    print(my_append(6))

    print('my_append2')
    print(my_append2(5))
    print(my_append2(6))

    print('my_append4')
    a = [1, 3, 4]
    my_append4(3, a)
    my_append4(7, a)
    print(a)

    print('my_append5')
    a = [1, 3, 4]
    my_append5(3, a)
    my_append5(7, a)
    print(a)

def rect2(a, b=None):
    if b is None:
        b = a
    return a * b

def rect2_test():
    print(rect2(4))  # 16
    print(rect2(2, 3))  # 6


def test_if(a, b=0):
    # ==, !=, >, <, >=, <=
    # and, or, not
    # is, in
    if a == 7:
        print('Yes, a == 7')
    elif a == 8:
        print('a != 7, but a == 8')
    else:
        print('Yes, a not == 7')

    if a == 7 and b == 0:
        print('7 0')

    a = [2, 3]
    b = a
    c = [2, 3]
    print(a == b, a is b)  # True True
    print(a == c, a is c)  # True False


def check_upper_lower(text):
    if text == text.upper():
        print('Upper')
    elif text == text.lower():
        print('Lower')
    else:
        print('None')


def check_while(a):
    while a > 1:
        print(a)
        a = int(a / 2)


def check_while2(a):
    while True:
        a = int(a / 2)
        if a % 4 == 0:
            continue
        print(a)
        if a <= 1:
            break


def check_for(my_list):
    summary = 0
    for x in my_list:
        print(x)
        summary += x
    print("summary", summary)


def check_for2(a):
    for x in range(a):
        print(x)


def check_for3():
    for x in range(5):
        print(x)

    print()
    for x in range(2, 5):
        print(x)

    print()
    print(list(range(5)))
    print(list(range(2, 5)))
    print(list(range(2, 10, 3)))


def for_containers():
    print('Tuple')
    a = (1, 3, 5)
    for x in a:
        print(x)

    print('List')
    a = [1, 3, 5]
    for x in a:
        print(x)

    print('Set')
    a = {1, 3, 5}
    for x in a:
        print(x)

    print('Dict')
    a = {'a': 1, 'b': 3, 'c': 5}
    for x in a:  # <==> for x in a.keys()
        print(x)

    for x in a.items():
        print(x, type(x))

    for key, val in a.items():
        print(key, 'has', val)


def print_dict(d):
    for key, value in d.items():
        print(f'key={key}, value={value}')


def for_containers2():
    my_dict = {'a': 1, 'b': 3, 'c': 5}
    my_list = ['Jan', 'Karol', 'Bartek', 'Adam']

    print('Enumerate list')
    for i, value in enumerate(my_list):
        print(i, value)

    print('Enumerate dict')
    for x in enumerate(my_dict.items()):
        print(x)

    print('Zip list')
    for a, b in zip(my_dict.items(), my_list):
        key, value = a
        print(a, b)

    print('Zip list2')
    for a, b in zip(my_list, my_dict.items()):
        print(a, b)


def test_for():
    # check_for([1, 3, 7])
    # check_for2(10)
    for_containers2()


def test_args(a, b, c, *d):  # d is tuple and takes all positional arguments
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))


def test_kwargs(a, b, c, **kwargs):  # kwargs is dict and takes all named arguments
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(kwargs, type(kwargs))


def test_args_kwargs(a, b, *args, c=3, d='d', **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(c, type(c))
    print(d, type(d))
    print(kwargs, type(kwargs))


def argsy_kwargsy():
    # print_dict({'abc': 3, 'Def': 5, 'xYx': 9, 'GGS': 14, 'XCY': 17, 'vgb': 99})  # key=abc, value=3
    # test_args(1, 'a', 4.5, 6, 1, 'haha', 19)
    # test_kwargs(a=1, b='a', c=4.5, d=6, e=1, f='haha', g=19)
    # test_args_kwargs(1, 5)
    # test_args_kwargs(1, 5, 6, 9, 10)
    # test_args_kwargs(1, 5, c=6, d=9, e=10)
    # test_args_kwargs(a=1, b=5, c=6, d=9, e=10)
    # test_args_kwargs(1, 5, 19, 20, c=6, d=9, e=10, f=30)
    # test_args_kwargs(1, 5, 19, 20, f=30)
    test_args_kwargs(z=30, a=1, b=2)


def convert_from_m_to_cm(x):
    return 100 * x


def convert_to_m(x, unit='m'):
    result = x
    if unit == 'cm':
        result = x / 100
    elif unit == 'km':
        result = x * 1000
    elif unit == 'mile':
        result = x * 1609
    elif unit == 'inch':
        result = x * 2.54 / 100
    return result


def convert_to_m2(x, unit='m'):
    multiplier = {'m': 1, 'cm': 0.01, 'km': 1000, 'mile': 1609, 'inch': 0.0254}
    return x * multiplier.get(unit)


def quadratic_equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        x0 = -b / 2 * a
        return x0
    else:
        delta_sqrt = delta ** (1/2)
        x1 = (-b - delta_sqrt) / (2 * a)
        x2 = (-b + delta_sqrt) / (2 * a)
        return x1, x2

argsy_kwargsy()

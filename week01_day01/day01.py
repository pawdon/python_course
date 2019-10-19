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

show_my_append()

# say_hello('Pawel')
# say_hello(5)
# say_hello2('Jan', 'Kowalski')
# say_hello('Jan', 'Nowak')
# say_hello('Jan')
# say_hello(first_name='Jan', age=22)
# say_hello(first_name='Jan',
#           age=22,
#          last_name='Nowak')

rect2(4)  # 16
rect2(2, 3)  # 6



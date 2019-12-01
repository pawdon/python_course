import numpy as np


def operations(x):
    print('\n', type(x))
    print(x)
    for i in x:
        print('\t', i)
    print(x[1])

    print('mul', 2 * x)
    x[0] = 13
    print(x)


def test_array():
    my_list = [3, 5, 7]
    my_array = np.array(my_list)
    operations(my_list)
    operations(my_array)

    print('arr', my_array)
    print('add', my_array + 3)
    print('pow', my_array ** 3)
    print('sin', np.sin(my_array))
    print('gt', my_array > 6)
    print('gt2', (my_array > 6) & (my_array < 10))
    # & <==> logical_and
    # | <==> logical_or
    print('gt2', np.logical_and(my_array > 6, my_array < 10))

    print()
    mask = my_array < 10
    print('arr', my_array)
    print('mask', mask)
    print('my_array[mask]', my_array[mask])
    my_array[mask] *= 2
    print('arr', my_array)
    my_array[mask] += 2
    print('arr', my_array)
    my_array[mask] += np.array([1, 2])
    print('arr', my_array)
    my_array[1:] += 7
    print('arr', my_array)



if __name__ == '__main__':
    test_array()

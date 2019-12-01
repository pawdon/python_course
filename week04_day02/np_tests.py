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

    my_array = np.where(my_array < 15, 2 * my_array, 3 * my_array)
    print('arr', my_array)

    arr2 = np.array(my_array)  # zawsze robi kopie; ta kopia jest np.ndarray
    arr3 = np.asarray(my_array)  # jesli dostanie np.ndarray, to zrobi referencje, a jesli liste, to utworzy np.ndarray
    print(arr2 == my_array, arr2 is my_array)
    print(arr3 == my_array, arr3 is my_array)

    arr4 = np.array(my_list)
    arr5 = np.asarray(my_list)
    print(arr4 == my_list, arr4 is my_list)
    print(arr5 == my_list, arr5 is my_list)



if __name__ == '__main__':
    test_array()

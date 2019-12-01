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


def my_fun(x):
    x = np.array(x)  # skopiuje, wiec zajmie wiecej czasu, wprost mozna zawolac np.copy(x)
    # x = np.asarray(x)  # zmieni obiekt na zewnatrz funkcji
    x += 5
    x[x > 10] -= 3
    x = x ** 2
    return x


def test_2d():
    my_list = [[1, 3, 5, 7], [2, 4, 6, 8], [11, 13, 15, 17]]
    print(my_list, '\n')
    arr = np.array(my_list)
    print(arr, '\n')
    print(arr + 2, '\n')
    print(arr / 2, '\n')
    arr2 = np.asarray(arr, dtype=np.float)
    print(arr is arr2, np.shape(arr2), arr2.dtype)
    arr2 /= 2
    print(arr2, '\n')

    print(arr, '\n')
    print(arr * arr, '\n')  # kazdy z kazdym
    print(arr @ arr.transpose(), '\n')  # mnozenie macierzowe, rownowazne z np.matmul(arr, np.transpose(arr))
    print(arr[2][3], '\n')
    print(arr[2, 3], '\n')
    print(arr[1:3, 2:], '\n')
    print(arr[:, 2], '\n')  # kolumna nr 2

    arr3 = np.array(range(12))
    print(arr3)
    print(arr3.reshape((-1, 6)))
    print(arr3.reshape((2, -1)))
    print(arr3.reshape((2, 2, -1)))


def operation2D_ver1(mat):
    a = mat[:, 0]
    b = mat[:, 1]
    c = a * b
    result = np.sum(c)
    print(mat, '\n')
    print(a, '\n')
    print(b, '\n')
    print(c, '\n')
    print(result, '\n')
    return result


def operation2D_ver2(mat):
    a = mat[:, 0]
    b = mat[:, 1]
    result = a @ b
    print(mat, '\n')
    print(a, '\n')
    print(b, '\n')
    print(result, '\n')
    return result


def operation2D_ver3(mat):
    a = mat[:, 0]
    b = np.array([mat[:, 1]]).transpose()
    result = a @ b
    print(mat, '\n')
    print(a, '\n')
    print(b, '\n')
    print(result, '\n')
    return result


def operation2D_ver4(mat):
    a = mat[:, 0]
    b = np.reshape(mat[:, 1], newshape=(-1, 1))
    result = a @ b
    print(mat, '\n')
    print(a, '\n')
    print(b, '\n')
    print(result, '\n')
    return result


if __name__ == '__main__':
    test_2d()

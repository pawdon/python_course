import functools
import time


GLOBAL_X = 5
USE_WRAPPERS = True

def my_fun01():
    print(GLOBAL_X)
    variable_y = 7

    def my_func_inner():
        print(GLOBAL_X, variable_y)

    my_func_inner()


def simple_wrapper(func):
    @functools.wraps(func)  # ta linia jest nieobowiazkowa, ale dobrze ja dodac; ukrywa uzycie wrappera
    def modified_func(*args, **kwargs):
        print('START')
        result = func(*args, **kwargs)
        print('STOP')
        return result

    if USE_WRAPPERS:
        return modified_func
    else:
        return func


@simple_wrapper
def my_fun():
    print('haha')


@simple_wrapper
def get_name():
    return 'Adam'


@simple_wrapper
def multiply(x, y):
    return x * y


def test_wrapper():
    # my_fun()
    # name = get_name()
    stime = time.time()
    mul = multiply(2, 3)
    dtime = time.time() - stime
    print('Czas', dtime, 's')
    print(mul)

    print(multiply)


if __name__ == '__main__':
    test_wrapper()

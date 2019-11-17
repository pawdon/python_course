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


class ABC:
    def do(self):
        pass

    def __str__(self):
        return 'haha'


def timed_wrapper(func):
    @functools.wraps(func)  # ta linia jest nieobowiazkowa, ale dobrze ja dodac; ukrywa uzycie wrappera
    def modified_func(*args, **kwargs):
        stime = time.time()
        result = func(*args, **kwargs)
        dtime = time.time() - stime
        print('Time', dtime, 's')
        return result

    return modified_func


@timed_wrapper
def long_fun():
    for i in range(10 ** 6):
        i *= 2


def wrapper_with_message(message):
    def proper_wrapper(func):
        @functools.wraps(func)
        def modified_func(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result
        return modified_func
    return proper_wrapper


@wrapper_with_message(message='Hello')
def multiply(x, y):
    return x * y


def test_wrapper():
    print(multiply(2, 3))
    print(multiply(2, 3))
    # long_fun()


if __name__ == '__main__':
    test_wrapper()

import functools
import time
from contextlib import contextmanager


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


def wrapper_with_message(message):
    def proper_wrapper(func):
        @functools.wraps(func)
        def modified_func(*args, **kwargs):
            # __name__ to sama nazwa funkcji; __qualname__ zawiera tez informacje o klasie itd
            print(message, func.__name__, func.__qualname__)
            result = func(*args, **kwargs)
            return result
        return modified_func
    return proper_wrapper


def timed_wrapper(filename, separator=','):
    def proper_wrapper(func):
        @functools.wraps(func)
        def modified_func(*args, **kwargs):
            stime = time.time()
            result = func(*args, **kwargs)
            dtime = time.time() - stime
            message = separator.join([func.__qualname__, str(dtime)]) + '\n'
            with open(filename, 'a+') as f:
                f.write(message)
            return result
        return modified_func
    return proper_wrapper


class ABC:
    @timed_wrapper(filename='time.csv')
    def do(self):
        pass

    def __str__(self):
        return 'haha'


@timed_wrapper(filename='time.csv')
def long_fun():
    for i in range(10 ** 6):
        i *= 2


@timed_wrapper(filename='time.csv')
def multiply(x, y):
    return x * y


def test_wrapper():
    print(multiply(2, 3))
    long_fun()
    print(multiply(2, 3))
    a = ABC()
    a.do()
    long_fun()
    # long_fun()


class ClassWith:
    def __init__(self, name):
        print('__init__')
        self.name = name

    def __enter__(self):
        print('Inside enter', self.name)
        return 7

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Inside exit', self.name)


def test_with():
    print('Start')
    obj = ClassWith('Adam')
    with obj as x:
        print('Inside with', x)
    print('Stop')


class ClassWith2:
    def __init__(self, name):
        print('__init__')
        self.name = name

    def __enter__(self):
        print('Inside enter', self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Inside exit', self.name)


def test_with2():
    print('Start')
    with ClassWith2('Adam') as x:
        print('Inside with', x.name)
    print('Stop')


@contextmanager
def context_funct(name):
    print('Begin', name)
    try:
        print('Try')
        yield 5
        print('After yield')
    finally:
        # jesli trzeba cos zamknac to tu
        print('End')


def test_with3():
    print('Start')
    with context_funct('Adam') as x:
        print('Inside with', x)
    print('Stop')


if __name__ == '__main__':
    test_with3()

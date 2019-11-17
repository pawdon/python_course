
GLOBAL_X = 5

def my_fun01():
    print(GLOBAL_X)
    variable_y = 7

    def my_func_inner():
        print(GLOBAL_X, variable_y)

    my_func_inner()


def simple_wrapper(func):
    def wrap():
        print('START')
        func()
        print('STOP')
    return wrap


@simple_wrapper
def my_fun():
    print('haha')


def test_wrapper():
    my_fun()


if __name__ == '__main__':
    test_wrapper()

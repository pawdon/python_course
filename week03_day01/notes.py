import functools


def my_wrapper01(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('START')
        result = func(*args, **kwargs)
        print('STOP')
        return result
    return wrapper


def my_wrapper02(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('START 2')
        result = func(*args, **kwargs)
        print('STOP 2')
        return result
    return wrapper


@my_wrapper02
@my_wrapper01
def my_function(name):
    print('Hello', name)


def gen1():
    for x in range(5):
        yield x


def gen2():
    print('Start')
    yield from gen1()
    print('Stop')


print(gen2())
for i in gen2():
    print(i)



    print(multiply.__qualname__)
    abc1 = ABC()
    abc2 = ABC()
    print(abc1.do.__qualname__)
    print(abc2.do)

    with open('haha.txt', 'a+') as f:
        f.write('xx\n')


def wrapper_with_message(message):
    def proper_wrapper(func):
        @functools.wraps(func)
        def modified_func(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result

        return modified_func

    return proper_wrapper

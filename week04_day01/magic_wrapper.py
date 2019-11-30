import functools


def magic_wrapper(func=None, name='XYZ'):
    def proper_wrapper(original_func):
        @functools.wraps(original_func)
        def modified_func(*args, **kwargs):
            print('Start', name)
            result = original_func(*args, **kwargs)
            print('Stop', name)
            return result
        return modified_func
    return proper_wrapper if func is None else proper_wrapper(func)


def multiply01(x, y):
    result = x * y
    print(f'{x} * {y} = {result}')
    return result

# multiply01 = magic_wrapper(multiply01) <~~> multiply01 = proper_wrapper(multiply01)
# multiply01 = magic_wrapper()(multiply01) <~~> multiply01 = proper_wrapper(multiply01)


@magic_wrapper
def multiply02(x, y):
    result = x * y
    print(f'{x} * {y} = {result}')
    return result


@magic_wrapper()
def multiply03(x, y):
    result = x * y
    print(f'{x} * {y} = {result}')
    return result


@magic_wrapper(name='ABC')
def multiply04(x, y):
    result = x * y
    print(f'{x} * {y} = {result}')
    return result


for fun in [multiply01, multiply02, multiply03, multiply04]:
    z = fun(3, 4)
    print(f'Result = {z}\n')

"""
3 * 4 = 12
Result = 12

Start XYZ
3 * 4 = 12
Stop XYZ
Result = 12

Start XYZ
3 * 4 = 12
Stop XYZ
Result = 12

Start ABC
3 * 4 = 12
Stop ABC
Result = 12
"""

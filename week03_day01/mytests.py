from contextlib import contextmanager


class XX:
    def __call__(self, *args, **kwargs):
        print('haha')


class YY:
    def __init__(self, y):
        self.y = y

    def __enter__(self):
        print('ENTER')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT Y', self.y)


# with YY(5) as y:
#     print('IN')


@contextmanager
def managed_resource(m, *args, **kwds):
    try:
        print('START', m)
        yield 7
        print('YIELD')
    finally:
        print('END')


with managed_resource(9) as f:
    print(f)

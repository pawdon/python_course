import week01_day02.day02
from week01_day02.dir01 import file_root_01, file_root_02
from week01_day02.dir01.dir01A import file01A
from week01_day02.dir01.dir01B import file01B
from week01_day02 import day02
from week01_day02.dir01.dir01B.file01B import *


def make_files_say_hello_simple():
    file_root_01.say_hello()
    file_root_02.say_hello()
    file01A.say_hello()
    file01B.say_hello()


def make_files_say_hello():
    print(type(file_root_01))
    for f in [file_root_01, file_root_02, file01A, file01B]:
        f.say_hello()

print('__name__', __name__)
if __name__ == '__main__':
    """
    print(week01_day02.day02.models)

    from week01_day02.day02 import colors
    print(colors)

    from week01_day02.day02 import doors_count as doors
    print(doors)

    from week01_day02 import day02
    print(day02.doors_count)

    from week01_day02.day02 import *
    print(get_engines_list(1.0, 2.5, 0.3))

    from week01_day02.dir01.file_root_01 import say_hello
    say_hello()"""
    make_files_say_hello()

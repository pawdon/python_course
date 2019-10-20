import week01_day02.day02

print('__name__', __name__)
if __name__ == '__main__':
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
    say_hello()

import argparse
import sys
import os
import shutil
import pathlib
import glob


def fun_arg01():
    print(sys.argv, type(sys.argv))


def fun_arg02():
    parser = argparse.ArgumentParser('Description of my function')
    parser.add_argument('abc', help='abc help')
    parser.add_argument('-def', help='def help')
    parser.add_argument('--ghi', help='def help')
    parser.add_argument('-j', '--jkl', help='jkl help')
    args = parser.parse_args()
    print(args)
    print(args.abc, type(args.abc))


def fun_arg03():
    parser = argparse.ArgumentParser('Description of my function')
    parser.add_argument('xyz', help='a help')
    parser.add_argument('-a', help='a help')
    parser.add_argument('-b', help='b help', required=True, type=int)
    parser.add_argument('-c', '--my_argument', help='c help', default=1.5, type=float)
    args = parser.parse_args()
    print(args)


def fun_arg04():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(a + b)


def fun_arg05():
    parser = argparse.ArgumentParser('Description of my function')
    parser.add_argument('a', help='a help', type=float)
    parser.add_argument('b', help='b help', type=float)
    args = parser.parse_args()
    print(args.a + args.b)


"""
python script.py 2.5 3.5  # 6; zrob 2 wersje (z uzyciem sys.argv i z uzyciem argparse)
"""


def test_os_01():
    dirname = '..'
    for filename in os.listdir(dirname):
        path = os.path.join(dirname, filename)
        # print(filename, path, os.path.abspath(path))
        if os.path.isdir(path):
            print(filename, os.listdir(path))
        else:
            print(filename)


def test_os_02():
    os.makedirs('new_dir', exist_ok=True)
    shutil.copy2('box_since_2000.csv', 'new_dir')
    shutil.copy2('box_since_2000.csv', 'new_dir/box.csv')
    os.remove('new_dir/box.csv')
    shutil.copytree('new_dir', 'new_dir2')
    shutil.rmtree('new_dir')


def test_os_03():
    my_path = 'abc/def/ghi.txt'
    print(os.path.split(my_path))
    print(os.path.splitext(my_path))
    print(pathlib.Path(my_path).parts)


def test_glob():
    for path in glob.iglob('../**/*.py', recursive=True):
        print(path)


if __name__ == '__main__':
    test_glob()

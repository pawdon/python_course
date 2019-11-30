import argparse
import sys


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


if __name__ == '__main__':
    fun_arg05()

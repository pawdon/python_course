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
    parser.add_argument('-c', help='c help', default=1.5, type=float)
    args = parser.parse_args()
    print(args)


"""
python script.py 2.5 3.5  # 6; zrob 2 wersje (z uzyciem sys.argv i z uzyciem argparse)
"""


if __name__ == '__main__':
    fun_arg03()

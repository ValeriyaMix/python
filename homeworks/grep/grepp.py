
import argparse
import sys


def output(line):
    print(line)

# def invert(lines, params):
#     if lines == params:
#          print('Sovpadaut')
#     else:
#          print(lines)
#     return lines, params
# def ignore_case():


def grep(lines, params):
    1pattern = params.pattern
    v = params.v
    i = params.i
    c = params.c
    n = params.n
    C = params.C
    B = params.B
    A = params.A

# Вывожу строки, которые не совпадают с шаблоном
    count = 0
    N = input('Vvedite N:')
    for line in lines:
        line = line.lower()
        pattern = pattern.lower()
        if pattern != line:
            # print(count+1)
            print(count+1,':', line)
            count += 1
    # print(count)
         # line+=1
     # invert(lines, params)
    # pass





def parse_args(args):
    parser = argparse.ArgumentParser(description='This is a simple grep on python')
    parser.add_argument(
        '-v', action="store_true", dest="invert", default=False, help='Selected lines are those not matching pattern.')
    parser.add_argument(
        '-i', action="store_true", dest="ignore_case", default=False, help='Perform case insensitive matching.')
    parser.add_argument(
        '-c',
        action="store_true",
        dest="count",
        default=False,
        help='Only a count of selected lines is written to standard output.')
    parser.add_argument(
        '-n',
        action="store_true",
        dest="line_number",
        default=False,
        help='Each output line is preceded by its relative line number in the file, starting at line 1.')
    parser.add_argument(
        '-C',
        action="store",
        dest="context",
        type=int,
        default=0,
        help='Print num lines of leading and trailing context surrounding each match.')
    parser.add_argument(
        '-B',
        action="store",
        dest="before_context",
        type=int,
        default=0,
        help='Print num lines of trailing context after each match')
    parser.add_argument(
        '-A',
        action="store",
        dest="after_context",
        type=int,
        default=0,
        help='Print num lines of leading context before each match.')
    parser.add_argument('pattern', action="store", help='Search pattern. Can contain magic symbols: ?*')
    return parser.parse_args(args)


def main():
    lines = ['tatata', 'RRrprrp', 'bymbymbym', 'lll']
    params = argparse.Namespace()
    params.pattern = 'taTata'
    params.n = True
    params.c = True
    params.h = False
    params.A = True
    params.B = False
    params.C = True
    params.v = False
    params.i = True
    grep(lines, params)
    #  params = parse_args(sys.argv[1:])
    #  grep(sys.stdin.readlines(), params)


if __name__ == '__main__':
    main()

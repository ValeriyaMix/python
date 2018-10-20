
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
    count = 0

    def context(do, posle):
        do = count



    def line_number():
        print(count+1 ':')

    def count():
        if pattern == line:
            count += 1


    def ignore_case():
        line = line.lower()
        pattern = pattern.lower()

    def invert():
        if pattern != line:
            print(line)

    for line in lines:
        if params.count:
            print(count())

        if params.invert:
            invert()

        if params.ignore_case:
            print(ignore_case())

        if params.line_number:
            line_umber()
    # pattern = params.pattern
  # Это мне помогли сделать, чтобы не запускать тесты из терминала, потому что у меня они почему-то не запускались
  #   v = params.v
  #   i = params.i
  #   c = params.c
  #   n = params.n
  #   C = params.C
  #   B = params.B
  #   A = params.A

# Это все, что я написала
    count = 0
    # N = input('Vvedite N:')
    # for line in lines:
    #     line = line.lower()
    #     pattern = pattern.lower()
    #     if pattern != line:
    #         # print(count+1)
    #         print(count+1,':', line)
    #         count += 1
        # else:
        #     do = count-int(N)
        #     posle = count+int(N)
        #     print(lines[do:posle])


    # print(count)
         # line+=1
     # invert(lines, params)
    # pass



#Это здесь уже было

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
    # Это опять тот кусок для проверки проги без терминала
    # lines = ['tatata', 'RRrprrp', 'bymbymbym', 'lll']
    # params = argparse.Namespace()
    # params.pattern = 'taTata'
    # params.n = True
    # params.c = True
    # params.h = False
    # params.A = True
    # params.B = False
    # params.C = True
    # params.v = False
    # params.i = True
    # grep(lines, params)

    # Это здесь уже было
    params = parse_args(sys.argv[1:])
    grep(sys.stdin.readlines(), params)

if __name__ == '__main__':
    main()

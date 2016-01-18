""" Main file for Calculator """

import sys
from tokenize import tokenize_line

DEFAULT_OUT = 'tmp.out'

def run():
    filename = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT

    in_file = open(filename, 'r')
    out_file = open(output_file, 'w')

    for line in in_file.readlines():
        out_file.write(line)
        tokenize_line(line)

    out_file.close()
    in_file.close()

if __name__ == '__main__':
    run()

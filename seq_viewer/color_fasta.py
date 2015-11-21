#!/usr/bin/env python
"""Show Fasta files in color
For example
./color_fasta.py mydb.fna
"""
from __future__ import print_function

import argparse
import re
from colored import bg, fg, attr


def parse_args():
    """Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Add color')
    parser.add_argument('fasta',  help='Input Fasta File Name')
    return parser.parse_args()


def main():
    args = parse_args()
    robj_A = re.compile('A+')
    robj_T = re.compile('T+')
    robj_G = re.compile('G+')
    robj_C = re.compile('C+')

    A_str = r'{}\g<0>{}'.format(fg('green'), attr(0))
    T_str = r'{}\g<0>{}'.format(fg('red'), attr(0))
    G_str = r'{}\g<0>{}'.format(fg('yellow'), attr(0))
    C_str = r'{}\g<0>{}'.format(fg('cyan'), attr(0))

    with open(args.fasta) as fi:
        for line in fi:
            line = line.rstrip()
            if line.startswith('>'):
                print(fg('black') + bg('grey_74') + line + attr(0))
            else:
                line.upper()
                line = robj_A.sub(A_str, line)
                line = robj_T.sub(T_str, line)
                line = robj_G.sub(G_str, line)
                line = robj_C.sub(C_str, line)
                print(line)


if __name__ == '__main__':
    main()

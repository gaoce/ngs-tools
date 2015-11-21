#!/usr/bin/env python
"""Show Fasta files in color
For example
./color_fasta.py mydb.fna
"""
from __future__ import print_function

import argparse
import re
from colored import fg, attr


def parse_args():
    """Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Add color')
    parser.add_argument('fasta',  help='Input Fasta File Name')
    return parser.parse_args()


def main():
    args = parse_args()

    color_A = '#d70000'
    color_T = '#ffaf5f'
    color_G = '#00ffff'
    color_C = '#0087af'

    def change_color(color):
        def repl(m):
            """Replace characters with blocks of the same length
            """
            return fg(color) + u'\u258D'*len(m.group(0)) + attr(0)
        return repl

    print(u'Legend: {}\u2588A{}  {}\u2588T{}  '
          u'{}\u2588G{}  {}\u2588C{}'.format(fg(color_A), attr(0),
                                             fg(color_T), attr(0),
                                             fg(color_G), attr(0),
                                             fg(color_C), attr(0)))

    with open(args.fasta) as fi:
        for line in fi:
            line = line.rstrip()
            if line.startswith('>'):
                print(line)
            else:
                line.upper()
                line = re.sub('A+', change_color(color_A), line)
                line = re.sub('T+', change_color(color_T), line)
                line = re.sub('G+', change_color(color_G), line)
                line = re.sub('C+', change_color(color_C), line)

                print(line)


if __name__ == '__main__':
    main()

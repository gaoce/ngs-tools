#!/usr/bin/env python
from __future__ import print_function

import sys
FLAGS = ["PAIRED       ", "PROPER_PAIR  ", "UNMAP        ", "MUNMAP       ",
         "REVERSE      ", "MREVERSE     ", "READ1        ", "READ2        ",
         "SECONDARY    ", "QCFAIL       ", "DUP          ", "SUPPLEMENTARY"]
FLAGS.reverse()

# Header
print("\t".join(FLAGS))

with open(sys.argv[1]) as file:
    for line in file:
        flag = line.strip()
        flag_bin = "{0:012b}".format(int(flag))
        print("\t".join(flag_bin))

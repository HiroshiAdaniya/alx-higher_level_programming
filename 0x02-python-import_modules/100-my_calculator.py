#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    length = len(sys.argv)
    if (length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if sys.argv[2] == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif sys.argv[2] == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

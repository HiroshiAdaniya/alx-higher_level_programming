#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0")
    elif i == 2:
        print("{}".format(sys.argv[1]))
    else:
        total = 0
        for j in range(1, i):
            total = total + int(sys.argv[j])
        print("{}".format(total))

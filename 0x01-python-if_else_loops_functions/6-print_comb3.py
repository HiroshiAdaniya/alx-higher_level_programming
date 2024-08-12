#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i == 8 and j == 9:
            break
        elif j < i:
            continue
        elif i != j:
            print("{}{}, ".format(i, j),  end='')
print("89")

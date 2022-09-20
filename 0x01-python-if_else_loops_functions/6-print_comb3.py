#!/usr/bin/python3
for a in range(9):
    for b in range(1, 10):
        if (b < a or b == a):
            continue
        if (a != 8):
            print("{:d}{:d}".format(a, b), end=', ')
        else:
            print("{:d}{:d}".format(a, b))

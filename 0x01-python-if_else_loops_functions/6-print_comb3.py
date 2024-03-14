#!/usr/bin/python3
for t in range(0, 9):
    for u in range(t + 1, 10):
        if t == 8:
            print("{:d}{:d}".format(t, u))
            break
        print("{:d}{:d}".format(t, u), end=", ")

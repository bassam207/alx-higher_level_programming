#!/usr/bin/python3

import sys


def add(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum


if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = [int(arg) for arg in sys.argv[1:]]
        result = add(*args)
        print(result)

    else:
        print("0")

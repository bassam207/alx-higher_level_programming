#!/usr/bin/python3

import sys


def count(arg):
    word_list = arg.split()
    no = len(word_list)

    if no == 0:
        print("0 arguments.")
    elif no == 1:
        print("{} argument:".format(no))
    else:
        print("{} arguments:".format(no))

    for i, item in enumerate(word_list, start=1):
        print("{}: {}".format(i, item))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
        count(arg)
    else:
        print("0 arguments.")

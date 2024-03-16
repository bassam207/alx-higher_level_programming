#!/usr/bin/python3

def main():
    def count(arg):
        _list = arg.split()
        no = len(_list)

        if no == 0:
            print("{} arguments.".format(no))
        elif no == 1:
            print("{} argument:".format(no))
        else:
            print("{} arguments:".format(no))

        for i, item in enumerate(_list, start=1):
            print("{}: {}".format(i, item))

    if __name__ == "__main__":
        main()

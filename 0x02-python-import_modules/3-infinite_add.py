#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argc = len(sys.argv)
    total = 0
    if argc == 1:
        print("{}".format(0))
    else:
        for i in range(1, argc):
            total = total + int(sys.argv[i])
        print("{}".format(total))

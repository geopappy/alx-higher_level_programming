#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argc = len(sys.argv)
    print("{} {} ".format(argc - 1, "argument" if argc == 2 else "arguments"))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))

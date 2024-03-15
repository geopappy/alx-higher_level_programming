#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    print("{} {} ".format(argc - 1, "argument" if argc == 2 else "arguments"))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))

#!/usr/bin/python3


def uppercase(str):
    for char in str:
        uppercase = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase), end="")
    print()

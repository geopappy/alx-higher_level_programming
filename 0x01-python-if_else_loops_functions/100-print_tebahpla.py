#!/usr/bin/python3

for char in range(ord('z'), ord('a')-1, -1):
    print("{}".format(chr(char - (0 if char % 2 == 0 else 32))), end="")

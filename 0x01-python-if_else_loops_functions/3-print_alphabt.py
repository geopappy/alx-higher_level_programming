#!/usr/bin/python3
'''Using a loop to iterate through ASCII values\
and printing the alphabet excluding 'q' and "e"'''
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in ['q', 'e']:
        print("{}".format(chr(i)), end="")

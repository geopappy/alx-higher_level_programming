#!/usr/bin/python3

def magic_string():
    magic_string.n  = geattr(magic_string, 'n', 0)
    return 'BestSchool' + ', BestSchool' * magic_string.n

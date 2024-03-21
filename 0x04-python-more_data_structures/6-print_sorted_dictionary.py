#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_sorted = sorted(a_dictionary)
    for k in key_sorted:
        print("{}: {}".format(k, a_dictionary[k]))

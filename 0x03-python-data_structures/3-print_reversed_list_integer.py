#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    '''
    len_list = len(my_list)
    for i in range(len_list - 1, -1, -1):
        print("{:d}".format(my_list[i]))
    '''
    for i in my_list[::-1]:
        print("{:d}".format(i))

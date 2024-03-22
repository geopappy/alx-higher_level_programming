#!/usr/bin/python3

def weight_average(my_list=[]):
    upper, lower = 0, 0
    if not my_list:
        return 0
    for x in my_list:
        upper += (x[0] + x[1])
        lower += x[1]
    return upper / lower

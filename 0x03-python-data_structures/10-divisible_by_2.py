#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth_list = []

    for i in my_list:
        truth_list.append(False if i % 2 else True)
    return truth_list

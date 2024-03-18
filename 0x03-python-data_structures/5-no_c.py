#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    new_string = ''

    if str_len > 0:
        for i in my_string:
            if i not in 'cC':
                new_string += i
        return (new_string)

#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    new_string = ''

    if str_len > 0:
        for i in range(str_len):
            if my_string[i] != 'c' and my_string[i] != 'C':
                new_string += (my_string[i])
        return (new_string)

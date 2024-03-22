#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':
                 1000}
    roman_list = list(roman_string.upper())
    prev_value, result = 0, 0
    for s in roman_list:
        if s not in roman_dic:
            return 0
        value = roman_dic[s]
        result += value
        if value > prev_value:
            result -= prev_value*2
            prev_value = value
    return result

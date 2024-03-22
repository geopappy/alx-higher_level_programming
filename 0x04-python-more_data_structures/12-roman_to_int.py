#!/usr/bin/python3
'''
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':
                 1000}
    roman_upper = reversed(roman_string.upper())
    prev_value, result = 0, 0
    for s in roman_upper:
        if s not in roman_dic:
            return 0
        value = roman_dic.get(s)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result '''


def roman_to_int(roman_string):
    """
    converts a roman numeral character into the respective integer
    """
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())
    result = 0
    prev = 0
    for letter in roman_list:
        if letter in roman_dict:
            result += roman_dict[letter]
            if roman_dict[letter] > prev:
                result -= prev * 2
            prev = roman_dict[letter]
        else:
            return (0)
    return (result)

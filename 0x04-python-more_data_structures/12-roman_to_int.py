#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    else:
        result = 0
        rmn = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in reversed(roman_string):
            num = rmn[i]
            result += num if result < num * 5 else -num
        return (result)

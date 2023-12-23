#!/usr/bin/env python3
def no_c(my_string):
    new_str = ''
    for f in my_string:
        if f != 'c' and f != 'C':
            new_str += f
    return (new_str)
        
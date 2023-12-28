#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        total = 0
        div = 0
        for x, y in my_list:
            total += x * y
            div += y
        return (total / div)

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        if i % 2 == 0:
            i = True
            result.append(i)
        else:
            i = False
            result.append(i)
    return (result)

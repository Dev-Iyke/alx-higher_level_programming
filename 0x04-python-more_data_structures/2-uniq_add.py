#!/usr/bin/python3
def uniq_add(my_list=[]):
    sm = 0
    for i in set(my_list):
        sm = sm + i
    return (sm)

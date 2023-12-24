#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ('None')

    length = len(my_list) - 1
    while length > 0:
        j = 0
        while j < length: 
            """ this loop is to check where that particular numbeer at the index of j after the current iteration """
            """ checking which value is greater """
            if my_list[j] > my_list[j + 1]:
                """ storing the current value and exchanging position """
                next = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = next
                """ it does not exchange positions """
            j += 1
            """ and enter next iteration """
            """ end of the round """
        length -= 1
    return (my_list[-1])

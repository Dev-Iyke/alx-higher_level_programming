#!/usr/bin/python3
# Here I am adding a private variable

""" Here is the Square """


class Square:
    """ Initializing the class """
    def __init__(self, size=0):
        """ creating a private attribute """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

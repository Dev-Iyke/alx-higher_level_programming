#!/usr/bin/python3
# Here I am adding a private variable

""" Here is the Square """


class Square:
    """ Initializing the class """
    def __init__(self, size=0):
        """ creating a private attribute """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)

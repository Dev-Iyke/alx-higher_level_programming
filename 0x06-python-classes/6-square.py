#!/usr/bin/python3
# Here I am adding a private variable

""" Here is the Square """


class Square:
    """ Initializing the class """
    def __init__(self, size=0, position=(0, 0)):
        """ creating a private attribute """
        self.__size = size
        self.__position = position
    """ Getter and setter for size """
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

    """ Getter and setter for position """
    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2 and not all(isinstance(i, tuple) and i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.__size == 0:
            return "\n"
        for w in range(self.__position[1]):
            pos += "\n"
        for w in range(self.__size):
            for i in range(self.__position[0]):
                pos += " "
            for j in range(self.__size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
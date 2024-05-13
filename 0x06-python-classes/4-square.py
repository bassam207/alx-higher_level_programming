#!/usr/bin/python3
"""Defines a class Square."""

class square:
    """Represents a square."""

    def __init__(self, size = 0):
        """Initializes a new square.

        Args:
        size (int): The size of the new square."""

        self.__size = size

        """ make getter method for size attribute"""

        @property
        def size(self):
            return (self.__size)
        """ make setter method for size attribute"""

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        """ make area method."""

        def area(self):
            return (self.__size **2)

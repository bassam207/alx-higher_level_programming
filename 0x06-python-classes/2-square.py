#!/usr/bin/python3
def __init__(self, size=0):
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


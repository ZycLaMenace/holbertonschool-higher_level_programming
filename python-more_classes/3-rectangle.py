#!/usr/bin/python3
"""Module for a class Rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__height = value

    def area(self):
        """Calcul and return area"""
        return self.width * self.height

    def perimeter(self):
        """Calcul perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''Returns a string representation of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):  # pour chaque ligne
            [rectangle.append('#') for j in range(self.__width)]  # x witdh
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

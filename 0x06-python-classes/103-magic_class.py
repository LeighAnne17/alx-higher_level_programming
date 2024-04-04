#!/usr/bin/python3
"""
Defines a MagicClass class that mimics the given Python bytecode.
"""
import math


class MagicClass:
    """
    Represents a MagicClass with similar behavior as described in the given bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a radius.

        Args:
            radius (int or float): The radius of the MagicClass instance.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius


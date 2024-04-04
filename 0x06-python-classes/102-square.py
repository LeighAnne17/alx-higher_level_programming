#!/usr/bin/python3
"""
Defines a Square class.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a square.

        Args:
            size (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if one square is less than the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is less than the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if one square is less than or equal to the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is less than or equal to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if one square is greater than the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is greater than the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one square is greater than or equal to the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the current square is greater than or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()


#!/usr/bin/python3

class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Override the == operator to return the inverted result.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to return the inverted result.
        """
        return super().__eq__(other)


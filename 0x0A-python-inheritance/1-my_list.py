#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from list and adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)


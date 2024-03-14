#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)
print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args)< end="")
print("{}".formnat("s"if num_args != 1 else ""), end="")
print("{}".format(":" if num_args != 0 else "."))
    
    if num_args > 0:
        foor i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))


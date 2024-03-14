#!/usr/bin/python3
import dis
import sys
if __name__ ="__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
    instructions = dis.get_instructions(code)
    names = set()
    for instruction in instructions:
        if instruction.opname == "LOAD_CONST":
            name = instruction.argval
            if isinstance(name, str) and not name.startwith("__"):
                names.add(name)
    for name in sorted(names):
        print(name)


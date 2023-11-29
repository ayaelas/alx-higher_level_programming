#!/usr/bin/python3
"""Test 4-print_square.py function"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

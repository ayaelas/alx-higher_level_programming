#!/usr/bin/python3
"""Module for say_my_name function"""


def say_my_name(first_name, last_name=""):
    """function prints first ans last name.


    Args:
        first_name: first name string.
        last_name: last name string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

print("My name is {:s} {:s}".format(first_name, last_name))

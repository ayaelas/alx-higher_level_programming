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
    print(f"My name is {first_name} {last_name}")

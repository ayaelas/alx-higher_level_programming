#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list 
    """
    length = len(list_of_integers)
    for i in range(1, length - 1):
        lis = list_of_integers[i]
        if (lis >= list_of_integers[i - 1] and lis >= list_of_integers[i + 1]):
            return lis

    return None

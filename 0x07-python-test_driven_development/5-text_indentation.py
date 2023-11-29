#!usr/bin/python3
"""Testing text_indentation function."""

def text_indentation(text):
    """ func to add 2 new lines after '.?:' chars."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    var = True
    for delim in text:
        if delim in "?.:":
            print(delim)
            print()
            var = True
        elif delim != ' ' or not var:
            print(delim, end="")
            var = False


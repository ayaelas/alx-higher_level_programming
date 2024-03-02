#!/usr/bin/python3
"""
list 10 commits of a repository
"""

import requests
import sys


if __name__ == "__main__":
    ze = sys.argv[1]
    solo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
                     ze, solo)

    ii = requests.get(url)
    j = ii.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                j[i].get("sha"),
                j[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

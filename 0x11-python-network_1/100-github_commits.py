#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

import requests
import sys


if __name__ == "__main__":
    ze = sys.argv[1]
    solo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
                     ze, solo)

    a = requests.get(url)
    v = a.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                v[i].get("sha"),
                v[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


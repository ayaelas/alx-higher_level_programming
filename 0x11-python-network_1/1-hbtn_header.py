#!/usr/bin/python3
"""
sends a request to the URL
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        val = response.getheader('X-Request-Id')
        print(val)


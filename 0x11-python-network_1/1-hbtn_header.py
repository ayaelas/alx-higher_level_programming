#!/usr/bin/python3
"""
- Takes in a URL + Sends a request to URL
"""
if __name__ == "__main__":
    import urllib.request as request
    import sys

    urlreq = request.Request(sys.argv[1])

    with request.urlopen(urlreq) as response:
        print(response.headers.get('X-Request-Id'))

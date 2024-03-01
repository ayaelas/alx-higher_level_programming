#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the passed email as parameter
"""
if __name__ == "__main__":
    import requests
    import sys

    dt = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], dt=data)
    print(response.text)

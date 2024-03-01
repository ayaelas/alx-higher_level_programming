#!/usr/bin/python3
"""
Takes GitHub credentials and display user's id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("None")

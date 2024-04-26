#!/usr/bin/python3
"""handle errors with requests"""

from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get(argv[1])
    try:
        res.raise_for_status()
    except requests.HTTPError:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)

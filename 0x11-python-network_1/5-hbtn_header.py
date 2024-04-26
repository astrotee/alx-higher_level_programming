#!/usr/bin/python3
"""get header value with requests"""

from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""handle errors"""

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        res = request.urlopen(argv[1])
    except error.HTTPError as e:
        print(f"Error code: {e.status}")
    else:
        with res:
            body = res.read()
            print(body.decode('utf-8'))

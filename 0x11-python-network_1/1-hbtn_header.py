#!/usr/bin/python3
"""get header value"""

from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        info = res.info()
        print(info.get("X-Request-Id"))

#!/usr/bin/python3
"""post email"""

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))

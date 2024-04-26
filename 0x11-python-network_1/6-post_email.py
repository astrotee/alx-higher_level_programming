#!/usr/bin/python3
"""post email with requests"""

from sys import argv
import requests

if __name__ == "__main__":
    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)

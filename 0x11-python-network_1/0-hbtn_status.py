#!/usr/bin/python3
"""get status"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        info = res.info()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

#!/usr/bin/python3
"""get status with requests"""

import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    body = res.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")

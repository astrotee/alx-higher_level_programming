#!/usr/bin/python3
"""search json api with requests"""

from sys import argv
import requests

if __name__ == "__main__":
    data = {'q': argv[1] if len(argv) > 1 else ''}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        res.raise_for_status()
        json = res.json()
        if len(json) == 0:
            print('No result')
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

#!/usr/bin/python3
"""query github user id"""

from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        res.raise_for_status()
        json = res.json()
        if len(json) == 0:
            print('No result')
        else:
            print(json.get('id'))
    except requests.HTTPError:
        print(None)
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

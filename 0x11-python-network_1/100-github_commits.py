#!/usr/bin/python3
"""query recent commits of a github repo"""

from sys import argv
import requests

if __name__ == "__main__":
    headers = {'Accept': 'application/vnd.github+json'}
    res = requests.get(
            f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits')
    try:
        res.raise_for_status()
        json = res.json()
        for r in json[:10]:
            print(f"{r.get('sha')}: {r['commit']['author'].get('name')}")
    except requests.HTTPError:
        print(None)
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

#!/usr/bin/python3
"""get all states"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.Connect('localhost', *sys.argv[1:])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
    for row in cur.fetchall():
        print(row)

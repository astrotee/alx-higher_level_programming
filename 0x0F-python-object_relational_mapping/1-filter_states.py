#!/usr/bin/python3
"""get all states starting with 'N'"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.Connect('localhost', *sys.argv[1:])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    for row in cur.fetchall():
        print(row)

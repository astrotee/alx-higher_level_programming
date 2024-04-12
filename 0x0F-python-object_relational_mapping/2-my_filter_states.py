#!/usr/bin/python3
"""get the given state"""

from sys import argv

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.Connect('localhost', *argv[1:4])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".
                format(argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

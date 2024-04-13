#!/usr/bin/python3
"""list all cities"""

from sys import argv

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.Connect('localhost', *argv[1:])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            LEFT JOIN states ON cities.state_id=states.id ORDER BY cities.id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

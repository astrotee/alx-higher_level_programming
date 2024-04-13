#!/usr/bin/python3
"""list cities of given state"""

from sys import argv

import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.Connect('localhost', *argv[1:4])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states \
            ON cities.state_id=states.id WHERE states.name LIKE BINARY %s \
                ORDER BY cities.id", (argv[4],))
    print(", ".join(r[0] for r in cur.fetchall()))
    cur.close()
    db.close()

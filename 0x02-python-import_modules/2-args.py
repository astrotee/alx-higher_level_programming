#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv) - 1
    print(f"{n} argument{'s' if n != 1 else ''}{':' if n else '.'}")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")

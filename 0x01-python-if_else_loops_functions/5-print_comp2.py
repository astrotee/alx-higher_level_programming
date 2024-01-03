#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        print("{}{}".format(i, j), end="")
        print(", " if i*j != 9*9 else "\n", end="")

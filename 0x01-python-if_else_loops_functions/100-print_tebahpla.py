#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr(ord('z') - i - (32 if i % 2 else 0))), end="")

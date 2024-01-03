#!/usr/bin/python3
for i in range(10):
    print("{}".format(", ".join(
        map(lambda x: str(i) + str(x), range(10)))),
        end="")
    print('\n' if i == 9 else ', ', end="")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
ld = ld - 10 if (number < 0 and ld) else ld
print(f"Last digit of {number} is {ld} and is ", end="")
if ld > 5:
    print("greater than 5")
elif ld == 0:
    print("0")
else:
    print("less than 6 and not 0")

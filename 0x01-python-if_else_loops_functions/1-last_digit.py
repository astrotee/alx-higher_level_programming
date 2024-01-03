#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
print(f"Last digit of {number} is {ld} and is {'not' if ld else ''} 0")

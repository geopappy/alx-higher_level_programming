#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
elif number < 0:
    print(f"{number: d} is negative")
else:
    print(f"{number: d} is zero")

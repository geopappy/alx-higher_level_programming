#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":

    import sys

    argc = len(sys.argv)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = (sys.argv[2])

    if opp not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if opp == "+":
        print("{} {} {} = {}".format(a, opp, b, add(a, b)))
    elif opp == "-":
        print("{} {} {} = {}".format(a, opp, b, sub(a, b)))
    elif opp == "*":
        print("{} {} {} = {}".format(a, opp, b, mul(a, b)))
    elif opp == "/":
        print("{} {} {} = {}".format(a, opp, b, div(a, b)))

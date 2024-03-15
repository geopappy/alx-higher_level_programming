#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":

    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = (sys.argv[2])

    if sys.agrv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if opp not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    match opp:
        case "+":
            print("{} {} {} = {}".format(a, b, add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a,       b, sub(a, b)))
        case "*":
            print("{} {} {} = {}".format(a,       b, mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a,       b, div(a, b)))

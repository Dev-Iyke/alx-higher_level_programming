#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    length = len(sys.argv) - 1

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif length == 3:
        for i in range(length):
            if sys.argv[2] != '+' or sys.argv[2] != '-' or sys.argv[2] != '*' or sys.argv[2] != '/':
                print("Unknown operator. Available operators: +, -, * and /")
            elif sys.argv[2] == '+':
                print("{} + {} = {}".format(a, b, ))

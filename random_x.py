#!/usr/bin/python3

# Will keep print lines of x where each line contains random characters of x from 5 to 19 inclusive until a line is printed with 16 or more characters

from random import randint 

def main():
    rand_x()


def rand_x():
    stringSize = 0
    while (stringSize < 16):
        stringSize = randint(5,19)
        output = "x" * stringSize
        print(output)

main()

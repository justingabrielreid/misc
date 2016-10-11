#!/usr/bin/python3

def draw_figure():
    for i in range(1, 11):
        for j in range(1, 11 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()
def draw_figure_2():
    for line in range(1, 6):
        for i in range(1, -4 * line + 21):
            print("/", end="")
        for i in range(1, 8 * line - 7):
            print("*",end="")
        for i in range(1, -4 * line + 21):
            print("\\",end="")
        print()

def main():
    draw_figure()
    print()
    draw_figure_2()

main()

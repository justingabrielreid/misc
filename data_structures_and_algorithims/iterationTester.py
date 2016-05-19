#!/usr/bin/python3

#Tester program that measures the number of iterations in the while loop


def iterationCalculator(problemSize):
    number = 0
    print ("%12s%16s" % ('Problem Size', 'Iterations'))
    while problemSize > 0:
        number += 1
        print("%12d%15s" % (problemSize, number))
        problemSize = problemSize // 2

def main():
    pSize = 4000
    for index in range(5):
        iterationCalculator(pSize)
        pSize = pSize * 2

if __name__ == '__main__':
    main()

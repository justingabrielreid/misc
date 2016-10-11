#!/usr/bin/python3

#Justin Reid 

def main():
    print_grid(2,4)
def print_grid(row, column):
    k = 0 
    for j in range(1, column + 1):
        for i in range(1, row + 1):
            k+=1
            print(str(k) + ',',\ )
        print('\t')


main()

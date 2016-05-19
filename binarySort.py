#!/usr/bin/python3

#example of a binary sort algorithm

def binarySort(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2 #integer division
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
            print(midpoint)
            # if less then search the bottom half of the list
        else:
            left = midpoint + 1
            print(midpoint)
            # if greater search the top half of the list
def main():
    integers = [20,44,55,62,66,74,88,93,99]
    print(binarySort(44 ,integers))

if __name__ == '__main__':
    main()

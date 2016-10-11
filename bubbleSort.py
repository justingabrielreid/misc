#!/usr/bin/python3

#An example of an algorithm using the bubble sort method:

#Swap function to change the position of two items
def swap(lyst, a, b):
	#exchanges position a with position b
	#assign position a to an intermediate value
	temp = lyst[a]
	lyst[a] = lyst[b]
	lyst[b] = temp
#--------------------------
'''
The bubble sort algorithm starts at the beginning of the list and compares pairs of data, swapping them if they are out of order. Has the effect of bubbling the largest items to the end of list.
'''
def bubbleSort(lyst):
    iterations = len(lyst)
    while iterations > 1: #perform n -1 iterations
#boolean marker to indicate whether any swaps have been done.
#If not swaps occur during the pass, then list has been sorted and the loop can end.
        swapFlag = False
        position = 1 #start at the second position in the list
        while position < iterations:
            '''
            if the value at the current position is less than the value at the position to the left of the current position then swap the two values. Change the swapFlag to True. The swapFlag exists to
            '''
            if lyst[position] < lyst[position - 1]:
                swap(lyst, position, position - 1)
                swapFlag = True
            position+=1
        if not swapFlag: return ''' exits the loop if not swaps occur, this indicates that the list is sorted '''
        iterations -= 1
def main():
    lyst = [1,5,7,9,0,4,8,3,6,2]
    bubbleSort(lyst)
    print (lyst)
if __name__ == '__main__':
    main()

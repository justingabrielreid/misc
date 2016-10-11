#!/usr/bin/python3

#An example of a selection sort algorithim

#Swap function to change the position of two items
def swap(lyst, a, b):
	#exchanges position a with position b
	#assign position a to an intermediate value
	temp = lyst[a]
	lyst[a] = lyst[b]
	lyst[b] = temp
#---------------------------------------------
def selectionSort(lyst):
	minIndex = 0
	while minIndex < len(lyst) - 1:
		currentIndex = minIndex + 1
		while currentIndex < len(lyst):
			if lyst[currentIndex] < lyst[minIndex]:
				swap(lyst, minIndex, currentIndex)
			currentIndex+=1
		minIndex+=1
#-------------------------------------------
def main():
	lyst = [1,5,7,9,0,4,8,3,6,2]
	print (lyst)
	selectionSort(lyst)
	print (lyst)
#-----------------------------------------
if __name__ == '__main__':
	main()

#!/usr/bin/python3
 
#program will take in a list of integers and move the zero values 
# to the back of the list without making a copy of the list and 
# maintaining the other values 

nums = [0,0,5,0,6,7,7,8,9,10,11,14,0,130,40,0,0,4,5]

for num in nums:
	if num == 0:
		nums.remove(num)
		nums.append(0)
print (nums) 
 






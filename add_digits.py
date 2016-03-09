#!/usr/bin/python

def main():
	print "Hello this program will add the digits of an integer until a singular digit is obtained"
	print 'For example 38 -> 3+8 = 11 -> 1+1 = 2. 2 will be returned'
	number = raw_input('Enter an integer value: ')
	print addDigits(number)

def addDigits(num):
	num_string = num
	sum_of_num = 0
	if len(num_string) > 1:
		for n in num_string:
			sum_of_num += int(n)
		num_s = str(sum_of_num)
		if len(num_s) > 1:
			addDigits(num_s)
		else:
			return int(num_s)			
	else:
		return int(num_string)
	
if __name__ == '__main__':
	main()





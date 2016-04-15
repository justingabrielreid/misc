#!/usr/bin/python3

def main():
	print ("Hello this program will add the digits of an integer until a singular digit is obtained")
	print ('For example 38 -> 3+8 = 11 -> 1+1 = 2. 2 will be returned')
	number = input('Enter an integer value: ')
	print (number + ' will reduce to ' + str(addDigits(number)))

def addDigits(num):
	sum_of_num = 0
	if len(num) == 1:
		return num 
	else: 
		for n in str(num):
			sum_of_num += int(n)
		return addDigits(str(sum_of_num))

    
if __name__ == '__main__':
    main()





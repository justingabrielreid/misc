#!/usr/bin/python

def main():
    print "Hello this program will add the digits of an integer until a singular digit is obtained"
    print 'For example 38 -> 3+8 = 11 -> 1+1 = 2. 2 will be returned'
    number = raw_input('Enter an integer value: ')
    print(number + " reduces to " + str(addDigits(number)))

def addDigits(num):
    if len(str(num)) == 1:
    	return num
    else:
        sum = 0
    	for n in str(num):
    		sum += int(n)

    	return addDigits(sum)
    
if __name__ == '__main__':
    main()

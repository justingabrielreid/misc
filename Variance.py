#!/usr/bin/python
def main():
	laps = {
		0: 1,
		1: 3,
		2: 3,
		4: 5,
		5: 8,
		6: 6,
		7: 2
    }
	laps2 = [0,1,1,1,2,2,2,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6,7,7]
	print variance(laps)
	print variance(laps2)

def variance(d):
	sum_of_vector = 0
	var = 0
	length = 0
	average = 0
	if type(d) is dict:
		for key in d:
			sum_of_vector += key*d[key]
		for key in d:
			length += d[key]
		average = sum_of_vector/ float(length)
		for key in d:
			var += (d[key]*(key - average)**2) / (length - 1)
		return var
	elif type(d) is list:
		length = len(d)
		for index in d: 
			sum_of_vector += index
		average = sum_of_vector / float(length)
		for index in d: 
			var += ((index - average)**2 / (length - 1))
		return var
if __name__ == '__main__':
	main()

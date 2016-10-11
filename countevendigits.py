#!/usr/bin/python3

#Justin Reid 

def main():
    print(count_even_digits(23456,5))
def count_even_digits(number, length):
    number_string = str(number)
    sum_of_even = 0 
    for i in range(0,length):
        x = int(number_string[i:i+1])
        if x % 2 == 0:
            sum_of_even+=1
    return sum_of_even
main()

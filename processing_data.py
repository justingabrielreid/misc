#!/usr/bin/python3 

#Section Homework 

def main():
    #Introduction to data processing, reading a file line by line
    file_name = open("integers.txt")
    process_data(file_name)
def process_data(fileName):
    line_sum = 0 
    num_lines = 0 
    lines = fileName.readlines()
    for line in lines:
        num_lines += 1 
        line_sum += int(line)
        print("Sum of " + str(num_lines) + " = " + str(line_sum))
    print("Average = " + str(line_sum/num_lines))

main()


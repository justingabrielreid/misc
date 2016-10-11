#!/usr/bin/python3
def main():
    print_triangle_type(5,7,7)
    print_triangle_type(3,4,8)
    print_triangle_type(5,5,5)

def print_triangle_type( side_1, side_2, side_3):
    if (side_1 == side_2) and (side_1 == side_3):
        print ("equilateral")
    if (side_1 == side_2) and (side_1 != side_3):
        print ("isosceles")
    if (side_1 != side_2) and (side_2 == side_3):
        print("isosceles")
    if (side_1 != side_2) and (side_1 != side_3) and (side_2 != side_3):
        print ("scalene")

main()


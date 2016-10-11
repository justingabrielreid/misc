#!/usr/bin/python3

#Justin Reid
#Homework 4 
#CSC 110

#This program calculates a student's course grade from inputs of their 
# 2 midterms, final exam and homework scores. 

def main():
    intro_statement()
    grade_calculator()

def intro_statement():
    print("This program reads exam/homework scoares and reports your overall course grade.")

def midterm_1():
    print("Midterm 1:")
    weight = float(input("Weight (0 -100) ? "))
    score = float(input("Score earned ? "))
    if score > 100:
        score = 100
    if_shift = int(input("Were scores shifted (1=yes, 2 = no) ? "))
    if if_shift == 1:
        score_shift = float(input("Shift amount ? "))
        if score + score_shift < 100:
            final_score = score + score_shift
        else:
            final_score = 100
    else:
        final_score = score
    weighted_score = ((final_score / 100) * weight)
    print("Total points = " + str(final_score) + " / 100")
    print("Weighted score = " + "{:.1f}".format((final_score/100)*weight) + " / " + str(weight)) 
    print()
    return weighted_score

def midterm_2():
    print("Midterm 2:")
    weight = float(input("Weight (0 -100) ? "))
    score = float(input("Score earned ? "))
    if score > 100:
        score = 100
    if_shift = int(input("Were scores shifted (1=yes, 2 = no) ? "))
    if if_shift == 1:
        score_shift = float(input("Shift amount ? "))
        if score + score_shift < 100:
            final_score = score + score_shift
        else:
            final_score = 100
    else:
        final_score = score
    weighted_score = ((final_score / 100) * weight)
    print("Total points = " + str(final_score) + " / 100")
    print("Weighted score = " + "{:.1f}".format((final_score/100)*weight) + " / " + str(weight)) 
    print()
    return weighted_score

def final():
    print("Final:")
    weight = float(input("Weight (0 -100) ? "))
    score = float(input("Score earned ? "))
    if score > 100:
        score = 100
    if_shift = int(input("Were scores shifted (1=yes, 2 = no) ? "))
    if if_shift == 1:
        score_shift = float(input("Shift amount ? "))
        if score + score_shift < 100:
            final_score = score + score_shift
        else:
            final_score = 100
    else:
        final_score = score
    weighted_score = ((final_score / 100) * weight)
    print("Total points = " + str(final_score) + " / 100")
    print("Weighted score = " + "{:.1f}".format((final_score/100)*weight) + " / " + str(weight))
    print()
    return weighted_score

def homework():
    print("Homework: ")
    weight = float(input("Weight (0 -100) ? "))
    num_assign = int(input("Number of assignments? " ))
    sum_of_points = 0.0
    sum_of_max_points = 0.0
    for num in range(1, num_assign + 1):
        points_earned = float(input("Assignment " + str(num) + " score? "))
        max_points = float(input("Assignment " + str(num) + " max? "))
        sum_of_points += points_earned 
        sum_of_max_points += max_points
    sessions_attended = int(input("How many sessions did you attend? "))
    if sessions_attended * 3 > 34:
        section_points = 34
    else:
        section_points = sessions_attended * 3 
    if sum_of_points > sum_of_max_points:
        sum_of_points = sum_of_max_points
    total_points = (sum_of_points + section_points) / (sum_of_max_points + 34)
    weighted_score = total_points * weight
    print("Section points = " + str(section_points) + " / 34")
    print("Total points = " + "{:.1f}".format((sum_of_points + section_points)) + " / " + "{:.1f}".format((sum_of_max_points + 34)))
    print("Weighted score = " + "{:.1f}".format(weighted_score) + " / " + "{:.1f}".format(weight))
    print()
    return weighted_score

def grade_calculator():
    overall_percentage = (midterm_1() + midterm_2() + final() + homework())
    print("Overall Percentage = " + "{:.1f}".format(overall_percentage))
    if overall_percentage >= 90.0:
        print("Your grade will be at least: A")
        print("Great job overachiever!")
    elif overall_percentage >= 80.0 and overall_percentage <  90.0:
        print("Your grade will be at least: B")
        print("You did better than most!")
    elif overall_percentage >= 70.0 and overall_percentage < 80.0:
        print("Your grade will be at least: C")
        print("C's get degrees")
    elif overall_percentage >= 60.0 and overall_percentage < 70.0:
        print("Your grade will be at least: D")
        print("At least you passed!")
    else:
        print("Your grade will be at least: E")
        print("Better luck next time!")


main()


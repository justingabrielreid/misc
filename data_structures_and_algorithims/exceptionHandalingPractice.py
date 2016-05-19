#!/usr/bin/python3

def safeIntegerInput(prompt):
    """ prompts the user for an integer and returns the integer if it is well formed. Otherwise, prints an error message an repeats this process. """
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print('Error in number format:', inputString)
        return safeIntegerInput(prompt)

if __name__ == "__main__":
    age = safeIntegerInput('Enter your age: ')
    print ("Your age is ", age)

#!/usr/bin/python3
# Author: Justin Reid 
# CSC 110 
# Homework 5 
# TA: Sujan 
# Sept 28th 2016
# Program will generate a random number and prompt the user to guess numbers 
# in the specified range until the user correctly guesses the random number 

from random import randint
def main():
    intro()
    # total_guesses is the number of guesses of all the games
    # initialized with the first game's guesses
    total_guesses = guess()
    # variable for the game with the lowest number of guesses
    best_game = total_guesses
    # counter for the number of games played 
    games_played = 1
    # prompt to play again
    response = input("Do you want to play again?")
    while(response[0] == "y" or response[0] == "Y"):
        #stores the current games number of guesses
        game = guess()
        total_guesses += game
        if (game < best_game):
            best_game = game
        games_played += 1 
        response = input("Do you want to play again?")
    stats(total_guesses, games_played, best_game)
# ------------------------------------------------------------
def intro():
    print("   Dark night grows longer")
    print("Time ebbs ever forward always")
    print("   I will sleep on time")
    print()    
#----------------------------------------------------------
def guess():
    print("I am thinking of a number between 5 and 25")
    rand_num = randint(5,25)
    number_of_guesses = 0
    user_guess = 0
    while(user_guess != rand_num):
        user_guess = int(input("Your guess? "))
        if (user_guess > rand_num):
            print( "It's lower.")
            number_of_guesses += 1
        elif (user_guess < rand_num):
            print("It's higher.")
            number_of_guesses += 1 
    if (user_guess == rand_num and number_of_guesses == 0):
        print("Yoou got it right in 1 guess!")
        number_of_guesses += 1
    elif (user_guess == rand_num):
            number_of_guesses += 1
            print("You got it right in " + str(number_of_guesses) + " guesses!")
    return number_of_guesses 
#-----------------------------------------------------------------
def stats(num_guesses, num_games, best_game):
    print("Total games = " + str(num_games) )
    print("Total guesses = " + str(num_guesses))
    print("Guesses/game = " + "{:.1f}".format(num_guesses/num_games))
    print("Best game = " + str(best_game))
#------------------------------------------------------------------------
main()


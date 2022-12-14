#!/usr/bin/env python

import random
import os
import time

def clear():
    os.system('clear')
# Set of instructions for Rock-Paper-Scissors
def rockpaperscissor_instructions():

	print("***********")
	print("Instructions for Rock-Paper-Scissors : ")
	print("***********")
	print("Rock crushes Scissors")
	print("Scissors cuts Paper")
	print("Paper covers Rock")
	print("***********")

def rockpaperscissor():
    options = ["rock", "paper", "scissors"]
    move = input("Enter your move: ")

    if move == "rock":
        print("Computer making it's move...")
        time.sleep(2)
        computerOption = random.choice(options)
        print("Computer chooses: ", computerOption)
        if computerOption == "rock":
            print("Match Ties")
            print("Thanks for playing the game...")
        elif computerOption == "paper":
            print("Computer wins")
            print("Thanks for playing the game...")
        elif computerOption == "scissors":
            print("You wins")
            print("Thanks for playing the game")
    elif move == "paper":
        print("Computer making it's move...")
        time.sleep(2)
        computerOption = random.choice(options)
        print("Computer chooses: ", computerOption)
        if computerOption == "rock":
            print("You wins")
            print("Thanks for playing the game...")
        elif computerOption == "paper":
            print("Match Ties")
            print("Thanks for playing the game...")
        elif computerOption == "scissors":
            print("Computer wins")
            print("Thanks for playing the game")
    elif move == "scissors":
        print("Computer making it's move...")
        time.sleep(2)
        computerOption = random.choice(options)
        print("Computer chooses: ", computerOption)
        if computerOption == "rock":
            print("Computer wins")
            print("Thanks for playing the game...")
        elif computerOption == "paper":
            print("You wins")
            print("Thanks for playing the game...")
        elif computerOption == "scissors":
            print("Match Ties")
            print("Thanks for playing the game")
    
    






name = input("Enter your name: ")

# The GAME LOOP
while True:

    # The Game Menu
    print("***********")
    print("Enter 1 to play Rock-Paper-Scissors")
    print("Enter 2 to quit")
    print("Enter 3 to read instructions")
    print("***********")

    # Try block to handle the player choice 
    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        clear()
        print("Wrong Choice")	
        continue

    # Play the traditional version of the game
    if choice == 1:
        clear()
        rockpaperscissor()

    # Quit the GAME LOOP 	
    elif choice == 2:
        break

    elif choice == 3:
        clear()
        rockpaperscissor_instructions()
    # Other wrong input
    else:
        clear()
        print("Wrong choice. Read instructions carefully.")

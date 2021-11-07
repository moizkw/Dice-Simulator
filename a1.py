# Author: Moiz Kharodawala, 500968133
# CPS109-06
# Assignment 1

# ~22 lines of comments
# ~45 lines of code
# Problem and Solution are described below
# All 5 learning objects completed (shown below after each)
# The code successfully solves the program
#          Check output.txt and the detailed explanations below 
# The code is my original work.
# So please give me a 100...thanks!

# Problem: Engineers study a lot and we really need a Ludo break from all the carnage. 
#          Unfortunately, I have the board of the game but I lost the dice.

# Solution: A dice simulator that solves the problem of having no physical dice. 
#           The code can be found below:

# Necessary Import
import random

# Required Function
# Learning Objective 5 completed
def moiz_dice_simulator():    
    
    #Initializing roll_it as true in the beginning so the dice can roll atleast once.
    roll_it = True 

    # While loop that makes sure that the dice rolls every time the user wishes
    # Used boolean primitive data type
    # Learning Objectives 2 & 4 completed
    while roll_it == True:

        # Generating a random digit between 1-6, which a dice is supposed to do
        # This is where we use our import
        result = random.randint(1,6) 

    # Implementing decisions using if statements
    # Learning Objective 1 completed        
        # First Condition
        if result == 1:
            print("-----------")
            print("|         |")
            print("|    ●    |")
            print("|         |")
            print("-----------")
        # Second Condition
        elif result == 2:
            print("-----------")
            print("|         |")
            print("|  ●   ●  |")
            print("|         |")
            print("-----------")
        # Third Condition
        elif result == 3:
            print("-----------")
            print("|    ●    |")
            print("|    ●    |")
            print("|    ●    |")
            print("-----------")
        # Fourth Condition
        elif result == 4:
            print("------------")
            print("|  ●    ●  |")
            print("|          |")
            print("|  ●    ●  |")
            print("------------")
        # Fifth Condition
        elif result == 5:
            print("-----------")
            print("| ●     ● |")
            print("|    ●    |")
            print("| ●     ● |")
            print("-----------")
        # Default Condition
        else:
            print("-----------")
            print("| ●     ● |")
            print("| ●     ● |")
            print("| ●     ● |")
            print("-----------")
        
        #Asking whether the user wishes to roll again
        roll_again = input("Enter 'y' to roll again or press any other key to exit: ") 
        
        # Comparing strings- 'roll_again' with 'y'
        # Learning Objective 3 completed
        if roll_again != 'y':
            # Continung the loop in case the user enters 'y'
            # And breaking the loop otherwise
            roll_it = False        
         
# Main Funtion
if __name__ == "__main__":

   #Welcome Message
   print("\nWelcome to Moiz's dice stimulator! \n") 
   #Calling our above function 
   moiz_dice_simulator()  
   # Good-bye Message
   print("\nThank you for using Moiz's dice simulator. I hope you won the game!\n")
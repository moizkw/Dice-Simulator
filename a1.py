# Author: Moiz Kharodawala, 500968133

# Necessary Import
import random

# Required Function
def moiz_dice_simulator():    
    
    #Initializing roll_it as true in the beginning so the dice can roll atleast once.
    roll_it = True 

    # While loop that makes sure that the dice rolls every time the user wishes
    # Used boolean primitive data type
    while roll_it == True:

        # Generating a random digit between 1-6, which a dice is supposed to do
        # This is where we use our import
        result = random.randint(1,6) 

    # Implementing decisions using if statements      
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
        if roll_again != 'y':
            # Continung the loop in case the user enters 'y'
            # And breaking the loop otherwise
            roll_it = False  
    #End of while loop
         
# Main Funtion
if __name__ == "__main__":

   #Welcome Message
   print("\nWelcome to Moiz's dice stimulator! \n") 
   #Calling our above function 
   moiz_dice_simulator()  
   # Good-bye Message
   print("\nThank you for using Moiz's dice simulator. I hope you won the game!\n")

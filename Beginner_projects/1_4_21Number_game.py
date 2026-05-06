#This is the 21 number game
import random
digits = [1,2,3] #This is an array to hold the number of allowed elements a player can add
guess = None
order=[] #array to hold the added elements

#function for the computer player
def computer_turn(order,digits):
    computer_guess = random.choice(digits)
        
    for _ in range(computer_guess):
           if order:
               new_value = order[-1] + 1
           else:
               new_value = 1
           order.append(new_value)  
           
           if new_value==21:
               break    
    print(f"After Computer's turn the numbers are: {order}") 
                
    if order[-1] >= 21:
        print("Computer lost! You have won!")
        return True
    return False

#game setup
print("-----WELCOME TO THE 21-NUMBER GAME!-----")
print("-----YOU WILL BE PLAYING WITH A COMPUTER. BE WISE AND HAVE FUN!-----")
    
print("""---RULES---
          1. You are going to be adding numbers to a list in ascending order from 1 until 21.
          2. You are allowed to add 1, 2 or 3 numbers in one entry. Do not repeat a number
          3. When it is your turn, you add your numbers and then a list showing
            all the added numbers so far will be displayed.
          4. The next turn is the computer's turn, the same rules apply to it.
          5. The first player to reach 21 is the loser. The goal is to not reach 21.""")
    
    
user_choice = input("\nEnter 'F' to take the first chance or 'S' to take the second chance:")
    
if user_choice=='F':
    while True:    
        entry = int(input("Enter how many numbers you want to add (1,2 or 3): "))
        if entry in digits:
            values= input(f"Enter {entry} numbers with spaces in between: ")
            new_values= [int(x) for x in values.split()] #change the inputs to integers from strings
                
            if 21 not in new_values and max(new_values)<21:
                order.extend(new_values)
                print(order)
                    
                if computer_turn(order,digits):
                    break    
            else:
                print("OOps you lost")
                break

elif user_choice=='S':
    while True:
        if computer_turn(order,digits):
            break
        entry = int(input("Enter a how many numbers you want to add (1,2 or 3): "))
        if entry in digits: #change the inputs to integers from strings
            values= input(f"Enter {entry} numbers with spaces in between: ")
            new_values= [int(x) for x in values.split()] #change the inputs to integers from strings
                
            if 21 not in new_values and max(new_values)<21:
                order.extend(new_values)
                print(order)         
            else:
                print("OOps you lost")
                break
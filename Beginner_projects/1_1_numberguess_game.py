import random
import math

def start_game():
    print("----------Welcome to the NUMBER GUESSING GAME!----------")
    
    #Collect user input: the starting and ending number for their range
    lower= int(input("Enter a starting number for your range: "))
    upper = int(input("Enter the last number for your range: "))
    print(f"Your range is {lower}-{upper}.")
    
    #Generate a random number within the user's range
    target = random.randint(lower,upper)
    
    #Calculate the maximum number of tries for the user
    n = upper+lower - 1
    max_guesses= math.ceil(math.log2(n))
    print(f"You have only {max_guesses} chances!")
    
    #The user guesses a number in their range
    user_guess=int(input("Guess a number:"))
    chances=0
    
    #Feedback loop for user 
    while chances<max_guesses:
        chances+=1
        if user_guess>target:
            print("Oh no, your guess was too high.")
        elif user_guess<target:
            print("Oh no, your guess was too low.")
        else:
            print(f"Congratulations, you took {chances} guesses")
            return
        user_guess=int(input("Guess again:"))    
    print(f"You have finished your chances! The number was {target}")
    
start_game()
    
    
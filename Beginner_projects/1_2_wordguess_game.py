import random
#This is the list of words that are randomly picked by the program.
words = ['axe','home','help','bottle','car','ear','candle','five','hire']

# This is a function to display the output based on the user's guess and how correct they are
def get_feedback(target,guess):
    feedback = []
    for i, letter in enumerate(guess):
        if i<len(target) and letter == target[i]:
            feedback.append(letter.upper())
        elif letter in target:
            feedback.append(letter.lower())    
        else:
            feedback.append("_")
    return "".join(feedback)   #put all elements in the array together to form a string

#this is a function to print a key for easy understanding      
def print_legend():
    print("KEY: \n")
    print("UPPERCASE means correct letter in correct psoition")
    print("lowercase means correct letter in wrong position")
    print("_ means letter does not exist in word")
    
#This is the main function of the game showing the logic    
def start_game():
    print("-----LET'S GUESS A WORD-----")
    #The program randomly picks a word from the list and the maximum chances for guessing is the length of the target word
    target = random.choice(words)
    max_chances = len(target)
    
    print(f"You have {max_chances} chances")
    print_legend()
    
    chance= 1
    won = False #assuming the user has not guessed anything yet
    while chance<=max_chances:
        user_guess = input(f"\nChance {chance}: ").strip().lower()
        chance+=1
        #if the user inputs a letter that might be in the word
        if len(user_guess)==1:
            if user_guess in target:
                print(f"{user_guess} is in the word")
            else:
                print(f"{user_guess} is not in the word")    
            
        #if the user inputs a word   
        else:
            #to check if the user's guess is not the same length as the target word
            if len(user_guess)!=len(target):
                print(f"Your guess must be {len(target)} letters long.")
              
            feedback=get_feedback(target,user_guess)
            print(f"Feedback: {feedback}")
        
            if user_guess==target:
                print(f"Congra congra! You guessed right using {chance-1} chance(s)!")
                won = True #the user has guessed correctly so the loop ends
                break
    #the loop ends because iterations are done        
    if not won:
        print(f"You have finished your chances! Correct word:' {target.upper()}'")    
        
#Player starts the game by calling game function
start_game()
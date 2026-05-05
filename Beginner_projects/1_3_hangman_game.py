import random
#List of words to be randomly selected by program
words = ['axe','home','help','bottle','car','ear','candle','five','hire']
#function to show the logic of game        
def start_game():
    print("-----LET'S PLAY HANGMAN-----")
    target = random.choice(words)
    max_chances = len(target) + 2
    #collection of correctly guessed letters in the target word
    correctly_guessed_letters = set()
    chance=1
    won = False #determine which print statement to display at end
    print(f"The word has {len(target)} letters")
    
    while chance<=max_chances:
        #this shows the current state of the word before the user guesses a letter
        display = [letter if letter in correctly_guessed_letters else '_' for letter in target]
        print("Word: ",''.join(display))
        
        user_guess = input(f"Chance {chance}: ").strip().lower()
        
        #the user should only enter one letter not many letters or symbol(s)
        if len(user_guess)!=1 or not user_guess.isalpha():
            print(f"Enter a single letter") 
            continue 
        #if the user has already guessed a letter that is correct, they shouldn't guess it again    
        if user_guess in correctly_guessed_letters:
            print("Your letter has already been guessed")  
            continue 
        
        chance+=1    
        #check if the letter exists in the target word, if yes then it is added to the correctly guessed letters     
        if user_guess in target:
            correctly_guessed_letters.add(user_guess)
            print(f"{user_guess} is in the word")
        else:
            print(f"{user_guess} is not in the word")
        #check that all the letters are in the target word    
        if all(letter in correctly_guessed_letters for letter in target):
            won=True
            print(f"Congratulations,you have guessed the word '{target}'")
            break
    if not won:
        print(f"Out of chances! Word is {target}")    

start_game()        
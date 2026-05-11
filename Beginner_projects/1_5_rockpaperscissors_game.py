#This is a simple rock paper scissors game where a user picks one of the options and the 
#computer chooses from the remaining options

import random
options = ['rock', 'paper', 'scissors']
remaining_options=[]

#function to generate the computer's choice
def computer_turn(options,user_guess):
    for i in (options):
        if i !=user_guess:
            remaining_options.append(i)
    return random.choice(remaining_options)

#function to generate the winner for each round
def get_winner(user_guess,computer_choice):
    if user_guess=='rock' and computer_choice=='scissors':
        return "user_guess"
    elif user_guess=='paper' and computer_choice=='rock':
        return "user_guess"
    elif user_guess=='scissors' and computer_choice=='paper':
        return "user_guess"
    elif user_guess==computer_choice:
        print("It's a Tie!")       
    else:
        return "computer_choice"

def play_game():
    user_score = 0
    computer_score = 0
    round = 1
    print("------LETS PLAY ROCK PAPER SCISSORS!------")
    
    #loop that runs as long as none of the players hasn't reached a score of 3
    while user_score<3 and computer_score<3:
        print(f"ROUND: {round}")
        print(f"YOUR SCORE: {user_score}  | COMPUTER_SCORE: {computer_score}")
        user_choice= input("Enter an option from (rock, paper, scissors): ").lower()
        
        #check if the user choice is valid
        if user_choice not in options:
            print("Invalid option")
            return 

        computer_choice= computer_turn(options,user_choice)
        print(f"Computer choice:  {computer_choice}")
        
        result=get_winner(user_choice,computer_choice)
        
        #condition to check the winner for each round
        if result=="user_guess":
            print(f"You have won round {round}")
            user_score+=1 #increase score by 1
        else:
            print(f"Computer has won round {round}")
            computer_score+=1  #increase score by 1
        round+=1 #increase round by 1
        
    #Overall result    
    if user_score==3:
        print("Congra congra! You are the overall winner")    
    else:
        print("Sorry, you lost overall")
       
play_game() 
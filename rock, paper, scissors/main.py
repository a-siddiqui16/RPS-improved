#Update the game to handle invalid inputs gracefully. For example, if the player enters something other than
#  "rock", "paper", or "scissors", prompt
#  them again until they provide valid input.

import random

player_count = 0
computer_count = 0

available_choices = ["rock", "paper", "scissors"]

while True:
    try:
        number_of_games = int(input("How many games of rock paper scissors would you like to play with the computer? "))
        break  # Exit the loop if the input is valid
    except Exception:
        print("Incorrect data type. Please enter a valid integer.")

    


#Gets the choices from the computer and the player    

def choices():
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors: ").lower()
        if player_choice in available_choices:
            break
        else:
            print("Invalid input! ")

    computer_choice = random.choice(available_choices)

    stored_choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return stored_choices

#Determines the winner

def get_winner(player, computer):

    global player_count, computer_count

    print(f"The player chose {player} and the computer chose {computer}")

    if player == computer:
        print("Its a tie! ")

    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors, you win! ")
            player_count += 1
        else:
            print("Paper covers rock, you lose! ")
            computer_count += 1

    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock, you win! ")
            player_count += 1
        else:
            print("Scissors cuts paper, you lose! ")
            computer_count += 1

    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper, you win! ")
            player_count += 1
 
        else:
            print("Rock smashes scissors, you lose! ")
            computer_count += 1



def results():

    global player_choice, computer_choice

    for i in range(0, number_of_games):
        result = choices()

        get_winner(result["player"], result["computer"])
        print(f"Current Score - Player: {player_count}, Computer: {computer_count}")

    # Final result
    print("Game over!")
    print(f"Final Score - Player: {player_count}, Computer: {computer_count}")

    f = open("results.txt", "a")
    f.write("Player score: " + str(player_count) + "\n")  
    f.write("Computer score: " + str(computer_count) + "\n")  
    f.close()
    

results()



    






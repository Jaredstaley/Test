import random
check = "yes"
r_p_s = ["rock","paper","scissors"]



while check == "yes":
    # Getting player choice and verifying it
    player = input("Enter a choice (rock, paper, scissors):").lower
    if player != "rock" and player != "paper" and player != "scissors":
        player = input("Kindly select appropriate option (rock, paper, scissors): ").lower
    
    # Gettigng computer choice
    computer = random.choice(r_p_s)
    
    #if both Computer and player chose the same its a tie
    if computer == player:
        print("Both players selected",computer,". It's a tie!")
    
    else:
        # Player choses Rock
        if player == "rock":
            if computer == "paper":
                win_lose = "lose"
                lose_reason = "covers"
            else:
                win_lose = "win"
                win_reason = "breaks"

        # If player chose paper 
        elif player == "paper":
            if computer == "scissors":
                win_lose = "lose"
                lose_reason = "cuts"
            else:
                win_lose = "win"
                win_reason = "covers"
            

        # If player chose scissors
        else:
            if computer == "rock":
                win_lose = "lose"
                lose_reason = "breaks"
            else:
                win_lose = "win"
                win_reason = "cuts"

        
        # Print result
        print("You chose",player,"computer chose",computer)
        if win_lose == "win":
            print(player, win_reason, computer,"! You win")
        else:
            print(computer, lose_reason ,player,"! You lose")

    #ask the user if they want to pay again
    check = input("Do you want to play another game?[yes or no]:")




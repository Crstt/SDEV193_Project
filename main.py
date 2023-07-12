import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        print("\nChoose your move: rock, paper, or scissors.")
        player_choice = input("Your choice: ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print("Computer's choice:", computer_choice)

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1

        print("Score: You", player_score, "- Computer", computer_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

play_game()

import random
def rpsls():
    playagain = True
    playerScore = 0
    computerscore = 0
    while playagain:
        validChoice = False
        possibleChoices = ["r","p","c","l","s"]
        choice = {"r":"Rock", "p":"Paper", "c":"Scissors","l":"Lizard","s":"Spock"}
        while not validChoice:
            playerChoice = input("Enter your Choice - (R)ock, (P)aper, S(c)issors, (L)izard, (S)pock: ")
            playerChoice=playerChoice.lower()
            if playerChoice in possibleChoices:
                validChoice = True
        computerChoice = possibleChoices[random.randint(0,4)]
        print("Player chose: " + str(choice.get(playerChoice)))
        print("Opponet chose: " + str(choice.get(computerChoice)))
        if playerChoice == computerChoice:
            print("It's a tie. You must try again")
        elif playerChoice== "c":
            if computerChoice == "p":
                print("Scissors cut Paper. You Win")
                playerScore += 1
            elif computerChoice == "l":
                print("Scissors decapitates Lizard. You win")
                playerScore += 1
            elif computerChoice == "r":
                print("Rock breaks Scissors. You lose")
                computerscore += 1
            else:
                print("Spock smashes Scissors. You lose")
                computerscore += 1
        elif playerChoice == "s":
            if computerChoice == "c":
                print("Spock smashes Scissors. You Win")
                playerScore += 1
            elif computerChoice == "r":
                print("Spock vaporizes Rock. You win")
                playerScore += 1
            elif computerChoice == "l":
                print("Lizard poisons Spock. You lose")
                computerscore += 1
            else:
                print("Paper disproves Spock. You lose")
                computerscore += 1
        elif playerChoice == "l":
            if computerChoice == "s":
                print("Lizard poisons Spock. You win")
                playerScore += 1
            elif computerChoice == "p":
                print("Lizard eats Paper. You win")
                playerScore += 1
            elif computerChoice == "r":
                print("Rock crushes Lizard. You lose")
                computerscore += 1
            else:
                print("Scissors decapitates Lizard. You lose")
                computerscore += 1
        elif playerChoice == "r":
            if computerChoice == "c":
                print("Rock breaks Scissors. You win")
                playerScore += 1
            elif computerChoice == "l":
                print("Rock crushes Lizard. You win")
                playerScore += 1
            elif computerChoice == "s":
                print("Spock vaporizes Rock. You lose")
                computerscore += 1
            else:
                print("Paper wraps Rock. You lose")
                computerscore += 1
        else:
            if computerChoice == "r":
                print("Paper wraps Rock. You win")
                playerScore += 1
            elif computerChoice == "s":
                print("Paper disproves Spock. You win")
                playerScore += 1
            elif computerChoice == "l":
                print("Lizard eats Paper. You lose")
                computerscore += 1
            else:
                print("Scisors cut Paper. You lose")
                computerscore += 1
        print("The current score is:\nPlayer: " + str(playerScore) + "\nComputer: " + str(computerscore))
        newgame = input("Would you like to go again? y/n - ")
        newgame=newgame.lower()
        if newgame == "n":
            if playerScore > computerscore:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Win!")
            elif computerscore > playerScore:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Lose!")
            else:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Tie!")
            playagain= False

rpsls()
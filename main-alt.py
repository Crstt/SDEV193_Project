import random

playagain = True
while playagain:
    validChoice = False
    possibleChoices = ["r","p","c","l","s"]
    choice = {"r":"Rock", "p":"Paper", "c":"Scissors","l":"Lizard","s":"Spock"}
    while not validChoice:
        playerChoice = input("Enter your Choice - (R)ock, (P)aper, S(c)issors, (L)izard, (S)pock: ")
        playerChoice=playerChoice.lower()
        if playerChoice in possibleChoices:
            validChoice = True
    computerChoice = possibleChoices[random.randint(0,5)]

    print("Player chose: " + str(choice.get(playerChoice)))
    print("Opponet chose: " + str(choice.get(computerChoice)))
    if playerChoice == computerChoice:
        print("It's a tie. You must try again")
    elif playerChoice== "c":
        if computerChoice == "p":
            print("Scissors cut Paper. You Win")
        elif computerChoice == "l":
            print("Scissors decapitates Lizard. You win")
        elif computerChoice == "r":
            print("Rock breaks Scissors. You lose")
        else:
            print("Spock smashes Scissors. You lose")
    elif playerChoice == "s":
        if computerChoice == "c":
            print("Spock smashes Scissors. You Win")
        elif computerChoice == "r":
            print("Spock vaporizes Rock. You win")
        elif computerChoice == "l":
            print("Lizard poisons Spock. You lose")
        else:
            print("Paper disproves Spock. You lose")
    elif playerChoice == "l":
        if computerChoice == "s":
            print("Lizard poisons Spock. You win")
        elif computerChoice == "p":
            print("Lizard eats Paper. You win")
        elif computerChoice == "r":
            print("Rock crushes Lizard. You lose")
        else:
            print("Scissors decapitates Lizard. You lose")
    elif playerChoice == "r":
        if computerChoice == "c":
            print("Rock breaks Scissors. You win")
        elif computerChoice == "l":
            print("Rock crushes Lizard. You win")
        elif computerChoice == "s":
             print("Spock vaporizes Rock. You lose")
        else:
            print("Paper wraps Rock. You lose")
    else:
        if computerChoice == "r":
            print("Paper wraps Rock. You win")
        elif computerChoice == "s":
            print("Paper disproves Spock. You win")
        elif computerChoice == "l":
            print("Lizard eats Paper. You lose")
        else:
            print("Scisors cut Paper. You lose")

    newgame = input("Would you like to go again? y/n - ")
    newgame=newgame.lower()
    if newgame == "n":
        playagain= False
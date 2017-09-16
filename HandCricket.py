import random

def welcome():
    print("Hi! I can't wait to play Hand Cricket with you!")
    s = getRightInput("Do you know how to play Hand Cricket? Y/N or y/n", ['Y', 'N', 'y', 'n'])
    if (s == 'N' or s == 'n'):
        print("No problem! Let's teach you how to play Hand Cricket!")
        tutorial()
    else:
        print("Awesome! Let's get right to it then!")
        play()

def getRunsPlayer():
    runs = 0
    while True:
        move1 = getMove()
        move2 = random.randint(1,6)
        if move1 == move2:
            return runs
        else:
            runs += move1
            print("Computer played " + str(move2))
            print("You played " + str(move1))
            print("Your total runs so far:", runs)

def getRunsComp():
    runs = 0
    while True:
        move2 = getMove()
        move1 = random.randint(1,6)
        if move1 == move2:
            return runs
        else:
            runs += move1
            print("Computer played " + str(move1))
            print("You played " + str(move2))
            print("Computer's total runs so far:", runs)
        
def tutorial():
    # Implement later
    print("vyebvykl")

def showVerdict(player, comp):
    print("\nGame Over. Verdict:")
    if player > comp:
        print("Congratulations, You Win!")
    elif comp > player:
        print("I win! Better luck next time!")
    else:
        print("Hehe it's a tie! Neither of us wins or loses! ")

def play():
    s = getRightInput("Would you like to Bat or Bowl? bat/bowl or Bat/Bowl", ["bat", "bowl", "Bat", "Bowl"])
    if(s in ['bat','Bat']):
        print("Alrighty then, I'll bowl!")
        playerRuns = getRunsPlayer()
        print("\nWhoops! You got out! Now it's my turn to bat!")
        print("You made " + str(playerRuns) + " runs. I need " + str(playerRuns+1) + " runs to win.")
        compRuns = getRunsComp()
        print("\nDrat! I got out!")
        showVerdict(playerRuns, compRuns)
    elif s == 'bowl' or s == 'Bowl':
        print("Alrighty then, you'll bowl!")
        compRuns = getRunsComp()
        print("\nWhoops! I got out! Now it's your turn to bat!")
        print("I made " + str(compRuns) + " runs. You need " + str(compRuns+1 )+ " runs to win.")
        playerRuns = getRunsPlayer()
        print("\nWhoops! You got out!")
        print("You made " + str(playerRuns) + " runs.")
        showVerdict(playerRuns, compRuns)

def getRightInput(input_string, list1):
    inp = input(input_string)
    if inp in list1:
        return inp
    else:
        print("Incorrect Input. Try Again.")
        return getRightInput(input_string, list1)

def getMove():
    try:
        move = int(input("Make your move. Enter a number between 1 and 6 (both inclusive):"))
        if move < 7 and move > 0:
            return move
        else:
            print("Incorrect Input. Try Again.")
            return getMove()
    except:
        print("Incorrect Input. Try Again.")
        return getMove()

welcome()


                   

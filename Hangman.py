# setup
from Screen import screen
import random
import os

# get list of words from file
with open("ListOfWords.txt") as file:
    words = file.read().splitlines()

# initialization
mainLoop = True
loopSentinel = True
lettersGuessed = []

#difficulty: 1=easy,2=normal,3=hard
difficulty = 2

timesWrong = 0

# testing output
def testDisplay():
    print("")
    print("Testing Display:")
    print("Current word: " + currentWord)
    print("Letters Revealed: " + createRevealed(currentWord, lettersGuessed))
    print("Letters Guessed: ")
    # sort lettersGuessed
    print(lettersGuessed)
    print("Wrong guesses: " + str(timesWrong))
    print("")
    
def createRevealed(word, guesses):  
    revealed = ""
    for i in word:
        if i in guesses:
            revealed += i
        else:
            revealed += "_ "
    return revealed
    
def clearScreen():
    if os.name == 'nt':        
        os.system('cls')
    else:        
        os.system('clear')
    
# main loop
# show title screen
clearScreen()
titleScreen = screen("gallows")
titleScreen.display()

# create gameScreen
gameScreen = screen("blank")

# mainLoop is the entire running process
while mainLoop == True:
    # game setup
    playerInput = input("Enter any key and press 'Enter' to continue or 'q' to quit: ") 
    if playerInput == 'q' or input == 'Q':
        print("Thanks for playing!")
        mainLoop = False
    else:
        # New Game
        loopSentinel = True
        # ask for difficulty(s) 
        while (playerInput != '1' and playerInput != '2' and playerInput != '3'):
            print("Choose a difficulty:")
            print("1) Easy")
            print("2) Normal") 
            print("3) Hard")
            playerInput = input("Select an action: ")     
        # pick currentWord at random from list
        currentWord = random.choice(words)
        
    # primary game loop
        while loopSentinel == True:            
            print("1) guess letter")
            print("2) guess word") 
            print("3) quit/restart")
            # get input
            # Clean input!
            playerInput = input("Select an action: ")
            # Clean input!
            if playerInput == '1':
                print(createRevealed(currentWord, lettersGuessed))
                gameScreen.display()
                testDisplay()
                # get input again
                # Clean input!
                playerInput = input("Guess a letter: ")
                if playerInput in lettersGuessed:
                    print("You already guessed that letter! Try again!")
                elif playerInput not in currentWord:
                    print("Wrong, that letter isn't in the word!")
                    lettersGuessed.append(playerInput)
                    gameScreen.addLetter(playerInput)
                    timesWrong += 1
                    # screen.addNextPart                    
                elif playerInput in currentWord:            
                    print("Correct! You got one!")
                    lettersGuessed.append(playerInput)
                    gameScreen.addLetter(playerInput)
                    testDisplay()                    
                    # screen.addNextPart
                else:
                    print("Error! You shouldn't be seeing this...")
                #check if timesWrong is greater than limit
                #   fail if it is
                
                # if createRevealed(currentWord, lettersGuessed) == currentWord
                #   you win!
            elif playerInput == '2':
                print("2")
                # get input
                # clean input
                playerInput = input("Enter your guess: ")
                if playerInput == currentWord:
                    # WIN SCREEN
                    # press enter to continue!
                    input("You win! Press 'Enter' to continue... ")                    
                else:
                    # WRONG!!
                    print("Wrong!")
            elif playerInput == '3':
                print("3")
                loopSentinel = False
                break
            else:
                print("errormessage")    
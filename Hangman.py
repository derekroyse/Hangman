# setup
from Screen import screen
import random

# get list of words from file
with open("ListOfWords.txt") as file:
    words = file.read().splitlines()

# initialization
mainLoop = True
loopSentinel = True
lettersGuessed = []
timesWrong = 0

# show title screen
#titleScreen = screen("title")
#titleScreen.display()

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

# main loop
while mainLoop == True:
    input = raw_input("Enter any key and press 'Enter' to continue or 'q' to quit: ") 
    if input == 'q' or input == 'Q':
        print("Thanks for playing!")
        mainLoop = False
    else:
        # New Game
        loopSentinel = True
        # pick currentWord at random from list
        currentWord = random.choice(words)
        while loopSentinel == True:            
            print("1) guess letter")
            print("2) guess word") 
            print("3) quit/restart")
            # get input 
            input = raw_input("Select an action: ")
            if input == '1':
                print(createRevealed(currentWord, lettersGuessed))
                testDisplay()
                # get input againt
                input = raw_input("Guess a letter: ")
                if input in lettersGuessed:
                    print("You already guessed that letter! Try again!")
                elif input not in currentWord:
                    print("Wrong, that letter isn't in the word!")
                    lettersGuessed.append(input)
                    timesWrong += 1
                    # screen.addNextPart                    
                elif input in currentWord:            
                    print("Correct! You got one!")
                    lettersGuessed.append(input)
                    # screen.addNextPart
                else:
                    print("Error! You shouldn't be seeing this...")                    
                #check if timesWrong is greater than limit
                #   fail if it is
                
                # if createRevealed(currentWord, lettersGuessed) == currentWord
                #   you win!
            elif input == '2':
                print("2")
                # get input
                # clean input
                # if input == currentWord
                    # WIN SCREEN
                # else:
                    # WRONG!!
            elif input == '3':
                print("3")
                loopSentinel = False
                break
            else:
                print("errormessage")    
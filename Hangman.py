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
timesWrong = 0

# difficulty parameters
#difficulty: 1=easy,2=normal,3=hard
difficulty = 2
maxWrong = 6

# set up difficulty parameters
def setDifficulty(difficultyOption):
    if difficultyOption == 1:
        maxWrong = 8
    elif difficultyOption == 2:
        maxWrong = 6
    elif difficultyOption == 3:
        maxWrong = 4
    else:
        # default to normal if invalid choice
        maxWrong = 6
        
    difficulty = difficultyOption

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
    
# Game progress display
def showInfo():
    print("Letters Revealed: " + createRevealed(currentWord, lettersGuessed))
    print("Guesses Remaining: " + str(maxWrong-timesWrong))
    
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
# TODO: show title screen
#clearScreen()
#titleScreen = screen("title")
#titleScreen.display()

# create gameScreen
gameScreen = screen("blank")

# mainLoop is the entire running process
while mainLoop == True:
    # game setup
    playerInput = raw_input("Enter any key and press 'Enter' to play or 'q' to quit: ") 
    if playerInput == 'q' or playerInput == 'Q':
        print("Thanks for playing!")
        mainLoop = False
    else:
        # New Game
        loopSentinel = True
        # ask for difficulty(s) 
        playerInput = 0
        while (playerInput != '1' and playerInput != '2' and playerInput != '3'):
            print("Choose a difficulty:")
            print("1) Easy")
            print("2) Normal") 
            print("3) Hard")
            playerInput = raw_input("Select a difficulty: ") 
        setDifficulty(playerInput)            
        # pick currentWord at random from list based on difficulty
        # TODO: change word choice based on difficulty
        currentWord = random.choice(words)        
    # primary game loop
        while loopSentinel == True: 
            clearScreen()
            gameScreen.display()
            print("Current Word: " + createRevealed(currentWord, lettersGuessed))
            showInfo()
            print("1) guess letter")
            print("2) guess word") 
            print("3) quit/restart") 
            # get input
            # TODO:  Clean input!
            playerInput = raw_input("Select an action: ")
            # TODO:  Clean input!
            if playerInput == '1':
                # get input again
                # TODO:  Clean input!
                playerInput = raw_input("Guess a letter: ")
                if playerInput in lettersGuessed:
                    print("You already guessed that letter! Try again!")
                elif playerInput not in currentWord:
                    print("Wrong, that letter isn't in the word!")
                    lettersGuessed.append(playerInput)                    
                    gameScreen.addLetter(playerInput)
                    timesWrong += 1                    
                    # TODO: Add next part to screen
                    # gameScreen.addNextPart                    
                elif playerInput in currentWord:            
                    print("Correct! You got one!")
                    lettersGuessed.append(playerInput)
                    gameScreen.addLetter(playerInput)
                else:
                    print("Error! You shouldn't be seeing this...")
                # check if timesWrong is greater than limit
                if (timesWrong > maxWrong):
                    # lose
                    clearScreen()
                    # loseScreen.display()                    
                    print("Dangnabbit we lost another one! Better luck next time!") 
                    raw_input("Press 'Enter' to continue... ")
                    loopSentinel = False
                    break     
                if createRevealed(currentWord, lettersGuessed) == currentWord:
                    # You win!
                    clearScreen()
                    # winScreen.display()
                    raw_input("YEEHAWW! You won! Press 'Enter' to continue... ")
                    loopSentinel = False
                    break    
            elif playerInput == '2':
                # get input
                # TODO:  clean input
                playerInput = raw_input("Enter your guess: ")
                # correct guess
                if playerInput == currentWord:
                    clearScreen()
                    # winScreen.display() 
                    raw_input("YEEHAWW! You won! Press 'Enter' to continue... ")
                    loopSentinel = False
                    break                    
                # incorrect guess
                else:                    
                    print("Well dang, that aint right! Keep at it, partner!")
                    raw_input("Press 'Enter' to continue... ") 
            elif playerInput == '3':
                loopSentinel = False
                break
            else:
                print("errormessage")    
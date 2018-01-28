from Screen import screen
import random
import os

# Create a dictionary to hold the positions of the letters 
# on the display board.
letterDict = dict()    
currentLetter = 'A'    
while currentLetter <= 'Z':
    for i in range(17, 66, 4):
        if currentLetter < 'N':
            letterDict[currentLetter] = 2,i
            currentLetter = chr(ord(currentLetter) + 1)
        else:
            letterDict[currentLetter] = 3,i
            currentLetter = chr(ord(currentLetter) + 1)   
# reference like thus: letterDict['A'][0] and letterDict['A'][1]

# get list of words from file
with open("ListOfWords.txt") as file:
    words = file.read().splitlines()

# initialization
mainLoop = True
loopSentinel = True
lettersGuessed = []
timesWrong = 0
victim = open("screens/victim.txt").readlines()

# create screens
titleScreen = screen("title")
loseScreen = screen("lose")
winScreen = screen("win")

# difficulty parameters
#difficulty: 1=easy,2=normal,3=hard
difficulty = 2
maxWrong = 5

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
    print("Current Word: " + createRevealed(currentWord, lettersGuessed))
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
clearScreen()
titleScreen.display()

# mainLoop is the entire running process
while mainLoop == True:    
    # game setup
    playerInput = raw_input("Press 'Enter' to continue or enter 'q' to quit: ") 
    if playerInput == 'q' or playerInput == 'Q':
        print("Thanks for playing!")
        mainLoop = False
    else:
        # New Game
        loopSentinel = True
        gameScreen = screen("gallows")
        # ask for difficulty(s) 
        #playerInput = 0
        #while (playerInput != '1' and playerInput != '2' and playerInput != '3'):
        #    print("Choose a difficulty:")
        #    print("1) Easy")
        #    print("2) Normal") 
        #    print("3) Hard")
        #   playerInput = raw_input("Select a difficulty: ") 
        #setDifficulty(playerInput)            
        # pick currentWord at random from list based on difficulty
        currentWord = random.choice(words)        
    # primary game loop
        while loopSentinel == True: 
            clearScreen()
            gameScreen.display()            
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
                    clearScreen()
                    lettersGuessed.append(playerInput)                    
                    gameScreen.addLetter(playerInput, letterDict)
                    timesWrong += 1                     
                    gameScreen.addNextPart(timesWrong, victim)                     
                    gameScreen.display()
                    print("Wrong, that letter isn't in the word!")
                    raw_input("Press 'Enter' to continue... ")
                elif playerInput in currentWord:            
                    clearScreen()
                    lettersGuessed.append(playerInput)
                    gameScreen.addLetter(playerInput, letterDict)
                    gameScreen.display()
                    
                    print("Correct! You got one!")
                    raw_input("Press 'Enter' to continue... ")
                else:
                    print("Error! You shouldn't be seeing this...")
                # check if timesWrong is greater than limit
                if (timesWrong > maxWrong):
                    # lose
                    clearScreen()
                    loseScreen.display()                    
                    print("Dangnabbit we lost another one! Better luck next time!") 
                    raw_input("Press 'Enter' to continue... ")
                    loopSentinel = False
                    break     
                if createRevealed(currentWord, lettersGuessed) == currentWord:
                    # You win!
                    clearScreen()
                    winScreen.display()
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
                    winScreen.display() 
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
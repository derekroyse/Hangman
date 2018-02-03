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

# Get list of words from file.
with open("ListOfWords.txt") as file:
    words = file.read().splitlines()

# Initialization.
maxWrong = 5
gameScreen = screen("gallows")
victim = open("screens/victim.txt").readlines()
exitGame = False

# Values reset with each new game.
continueGame = True
lettersGuessed = []
timesWrong = 0
globalCurrentWord = "temp"

# Create screens.
titleScreen = screen("title")
loseScreen = screen("lose")
winScreen = screen("win")
gameScreen = screen("gallows")
    
# Game progress display.
def showInfo():
    print("Letters Revealed: " + createRevealed(currentWord, lettersGuessed))
    print("Incorrect Guesses Remaining: " + str(maxWrong-timesWrong))

# Create a string to show which letters in the current
# word have been revealed.    
def createRevealed(word, guesses):  
    revealed = ""
    for i in word:
        if i in guesses:
            revealed += i
        else:
            revealed += "_ "
    return revealed

# Clear the screen based on operating system.    
def clearScreen():
    if os.name == 'nt':        
        os.system('cls')
    else:        
        os.system('clear')
        
# Reset game values (for a new game).
def resetGame():
    global continueGame
    global gameScreen
    global timesWrong
    global lettersGuessed
    global currentWord
    
    continueGame = True
    gameScreen = screen("gallows") 
    timesWrong = 0
    lettersGuessed = []
    # Pick currentWord at random from the word list.
    currentWord = random.choice(words)      

    
    
# Game/new game loop.
clearScreen()
titleScreen.display()
while exitGame == False:    
    # Game Setup
    playerInput = 'x'
    playerInput = raw_input("Press 'Enter' to continue or enter 'q' to quit: ") 
    if playerInput == 'q' or playerInput == 'Q':
        print("Thanks for playing!")
        exitGame = True
    else:
        # Setup a new game.
        resetGame()
    # Primary game loop.
        while continueGame == True: 
            # Reset the display.
            clearScreen()
            gameScreen.display()            
            showInfo()
            # Print actions.
            print("1) Guess a letter.")
            print("2) Guess the word.") 
            print("3) Quit or restart.")
            # Get input.
            playerInput = raw_input("Select an action: ")
            
            # Option 1: Player guesses a letter.
            if playerInput == '1':
                # Get input.
                playerInput = raw_input("Guess a letter: ")
                # Incorrect input.
                if not playerInput.isalpha():
                    print("Invalid input! Please enter a letter.") 
                    raw_input("Press 'Enter' to continue... ")
                # Player already guessed the letter.
                elif playerInput in lettersGuessed:
                    print("You already guessed that letter! Try again!")
                    raw_input("Press 'Enter' to continue... ")
                # Letter not in word.
                elif playerInput not in currentWord:
                    clearScreen()
                    lettersGuessed.append(playerInput)                    
                    gameScreen.addLetter(playerInput, letterDict)
                    timesWrong += 1                     
                    gameScreen.addNextPart(timesWrong, victim)                     
                    gameScreen.display()
                    print("Wrong, that letter isn't in the word!")
                    raw_input("Press 'Enter' to continue... ")
                # Letter is in word.
                elif playerInput in currentWord:            
                    clearScreen()
                    lettersGuessed.append(playerInput)
                    gameScreen.addLetter(playerInput, letterDict)
                    gameScreen.display()                    
                    print("Correct! You got one!")
                    raw_input("Press 'Enter' to continue... ")
                
                # Check if timesWrong is greater than limit.                
                if (timesWrong >= maxWrong):
                    # You lose!
                    clearScreen()
                    loseScreen.display()                    
                    print("Dangnabbit we lost another one! Better luck next time!") 
                    raw_input("Press 'Enter' to continue... ")
                    continueGame = False
                    break     
                # Check if player has revealed all letters in the word.
                if createRevealed(currentWord, lettersGuessed) == currentWord:
                    # You win!
                    clearScreen()
                    winScreen.display()
                    raw_input("YEEHAWW! You won! Press 'Enter' to continue... ")
                    continueGame = False
                    break    
            # Option 2: Player attempts to guess the word.
            elif playerInput == '2':
                # Get input.
                playerInput = raw_input("Enter your guess: ")
                # Correct guess.
                if playerInput == currentWord:
                    clearScreen()
                    winScreen.display() 
                    raw_input("YEEHAWW! You won! Press 'Enter' to continue... ")
                    continueGame = False
                    break                    
                # Incorrect guess.
                else:                    
                    print("Well dang, that aint right! Keep at it, partner!")
                    raw_input("Press 'Enter' to continue... ") 
            # Option 3: Player chooses to exit the current game.
            elif playerInput == '3':
                continueGame = False
                break
            # Player enters a value that isn't 1, 2, or 3.
            else:
                print("Please enter the number corresponding to your choice.")
                raw_input("Press 'Enter' to continue... ")                
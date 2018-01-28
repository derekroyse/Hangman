import sys
from string import ascii_uppercase

# The screen class allows a user to create a Screen object
# by passing it the filename of a text file. Contains
# methods to print the screen and add things to it.
class screen:
    # Source is a list that contains the data that is
    # printed to the screen.
    source = []
              
    def __init__(self, filename):
        fileString = "screens/" + filename + ".txt"
        with open(fileString, "r") as f:
            ## for line in f
                ## make an iterator
                ## self.source[iterator] = list(f)
            self.source = f.readlines()
            #self.source = list(f.readlines())
    
    # Print out a screen.
    def display(self):
        for line in self.source:
            sys.stdout.write(line)
        print(" ")
        print(" ")
            
    # Add a guessed letter to the appropriate position on
    # the screen.
    def addLetter(self, letter, letterDict):
        letter = letter.upper()
        tempList = list(self.source[letterDict[letter][0]])
        tempList[letterDict[letter][1]] = letter
        self.source[letterDict[letter][0]] = ''.join(tempList)
    
    # Based on how many incorrect guesses have been made,
    # add the appropriate hangman part to the Screen.
    def addNextPart(self, number, victim):
        if number == 1:
            # Add hat to hangman.
            # Lines 7,8, and 9.          
            for i in range(7, 10):
              self.source[i] = victim[i]
        elif number == 2:
            # Add head to hangman.
            # Lines 10, 11, 12, 13.
            for i in range(10, 14):
              self.source[i] = victim[i]
        elif number == 3:
            # Add body to hangman.
            # .ines 14, 15, 16, 17, 18, 19, 20.
            for i in range(14, 21):
              self.source[i] = victim[i]
        elif number == 4:
            # Add legs to hangman.
            # Lines 21, 22, 23, 24, 25.
            for i in range(21, 26):
              self.source[i] = victim[i]       
        elif number == 5:
            # Add boots to hangman.
            # Lines 26, 27, 28.
            for i in range(26, 29):
              self.source[i] = victim[i] 
        else:
            print("Whoops!")     
     
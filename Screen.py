import sys
from string import ascii_uppercase
from pprint import pprint

class screen:
    source = []                   
    base = []
    hat = []
    head = []
    body = []
    lArm = []
    rArm = []
    lLeg = []
    rLeg = []
    boots = []
    
    # Create a dictionary to hold the positions of the letters
    letterDict = dict()    
    currentLetter = 'A'    
    while currentLetter <= 'Z':
        for i in range(17, 66, 4):
            if currentLetter < 'N':
                letterDict[currentLetter] = 3,i
                currentLetter = chr(ord(currentLetter) + 1)
            else:
                letterDict[currentLetter] = 4,i
                currentLetter = chr(ord(currentLetter) + 1)   
    # reference like thus: letterDict['A'][0] and letterDict['A'][1]
    
    def dictTest(self):
        pprint(self.letterDict)
                    
    def __init__(self, filename):
        fileString = "screens/" + filename + ".txt"
        with open(fileString, "r") as f:
            self.source = f.readlines()
        
    def display(self):
        for line in self.source:
            sys.stdout.write(line)
        print(" ")
        print(" ")
            
    def addLetter(self, letter):
        letter = letter.upper()
        self.letterDict[letter][0]
        tempList = list(self.source[self.letterDict[letter][0]])
        tempList[self.letterDict[letter][1]] = letter
        self.source[self.letterDict[letter][0]] = ''.join(tempList)
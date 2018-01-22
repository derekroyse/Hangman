import sys
from string import ascii_uppercase
from pprint import pprint

class screen:
    source = []
    hat = ["|             |||                    /\_|_/\                                  |\n",
           "|             |||                   |       |                                 |\n",
           "|             |||                (__|_______|__)                              |\n"]
    head = ["|             |||                  (  O   O  )                                |\n",
            "|             |||                   |   -   |                                 |\n",
            "|             |||                   |  ___  |                                 |\n",
            "|             |||                    \__|__/                                  |\n"]
    body = ["|             |||                    __| |__                                  |\n",
            "|             |||                   /  \ /  \                                 |\n",
            "|             |||                  /    V    \                                |\n",
            "|             |||                 | |       | |                               |\n",
            "|             |||                 | |       | |                               |\n",
            "|             |||                 |_|       |_|                               |\n",
            "|             |||                  \|_______|/                                |\n"]
    legs = ["|             |||                   (|||O|||)                                 |\n",
            "|             |||                    |     |                                  |\n",
            "|             |||                    |  V  |                                  |\n",
            "|             |||                    |  |  |                                  |\n",
            "|             |||                    |__|__|                                  |\n"]
    boots = [ "\            |||                    |  |  |                                  /\n",
              " \        ||||||||||                |  |  |                                 /\n",
              "  \       ||||||||||              <___/*\___>                              /\n"]
    
    # Create a dictionary to hold the positions of the letters
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
    
    def dictTest(self):
        pprint(self.letterDict)
                    
    def __init__(self, filename):
        fileString = "screens/" + filename + ".txt"
        with open(fileString, "r") as f:
            self.source = f.readlines()
            #self.source = list(f.readlines())
        
    def display(self):
        for line in self.source:
            sys.stdout.write(line)
        print(" ")
        print(" ")
            
    def addLetter(self, letter):
        letter = letter.upper()
        tempList = list(self.source[self.letterDict[letter][0]])
        tempList[self.letterDict[letter][1]] = letter
        self.source[self.letterDict[letter][0]] = ''.join(tempList)
    
    def addNextPart(self, number):
        if number == 1:
            self.addHat()
        elif number == 2:
            self.addHead()
        elif number == 3:
            # addBody
             print("3")
        elif number == 4:
            # addLegs
             print("4")
        elif number == 5:
            # addBoots
             print("5")
        else:
            print("Whoops!")
    
    def addHat(self):
        # lines 7,8, and 9
        self.source[7] = self.hat[0]
        self.source[8] = self.hat[1]
        self.source[9] = self.hat[2]
    
    def addHead(self):
        # lines 10, 11, 12, 13
        self.source[10] = self.head[0]
        self.source[11] = self.head[1]
        self.source[12] = self.head[2]
        self.source[13] = self.head[3]
        
    
        
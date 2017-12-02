import sys

class screen:
    source = []
    letterArray = ["A B C D E F G H I J K L M",
                   "N O P Q R S T U V W X Y Z"]
                   
    base = []
    hat = []
    head = []
    body = []
    lArm = []
    rArm = []
    lLeg = []
    rLeg = []
    boots = []
                    
    def __init__(self, filename):
        fileString = "screens/" + filename + ".txt"
        with open(fileString, "r") as f:
            self.source = f.readlines()
        
    def display(self):
        for line in self.source:
            sys.stdout.write(line)
        print(" ")
        print(" ")
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
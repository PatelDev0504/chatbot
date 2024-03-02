import re
class Data:
    def __init__(self, name, regexStart, regexEnd): #constructor
        self.name = name
        self.regexStart = regexStart
        self.regexEnd = regexEnd
    
    def printString(self, fileName):
        #initalizes the regular expression for the start
        regexStart = re.compile(self.regexStart)
        #initalizes the regular expression for the end
        regexEnd = re.compile(self.regexEnd)
        #creates a boolean value to determine whether the file reader is inbetween the start and end
        isWithin = False
        with open(fileName, "r") as f: #opens the file reader
            with open("../data/output.txt", "a") as g: #opens the file writer
                for line_i, line in enumerate(f, 1): #iterating through the file one line at a time
                    if regexStart.search( line ): #checking the line to see if the start regex is contained within it
                        isWithin = True #changes the boolean value to true
                    if regexEnd.search( line ): #checking the line to see if the end regex is contained within it
                        isWithin = False #changes the boolean value to be false again
                    if (isWithin): #checks the boolean value to ensure that the file reader is between the start and end regex
                        g.write(line) #prints the line to the output file
        f.close() #closes the file reader
        g.close() #closes the file writer
    
    def retName(self): #getter for the name
        return self.name
    
from fuzzywuzzy import fuzz #importing fuzz from fuzzbuzz
import Data
import sessionStatistics
import re

def findIfQuit(q, currentSession):
    #creates a list of quit prompts
    quitPrompts = ["QUIT", "LEAVE", "GO AWAY", "STOP", "EXIT", "Q", "BYE"]
    highestRatio = -1000 #sets highestRatio to be negative
    for x in quitPrompts: #iterates through the list
        ratio = fuzz.partial_ratio(x, q) #uses a string matching algorithm from fuzzywuzzy 
        if (ratio > highestRatio): #checks to see if the ratio is greater than highestRatio
            highestRatio = ratio #sets the highestRatio to ratio
    if (highestRatio >= 90): #checks to see if highestRatio is greater than or equal to 90
        with open(currentSession, 'a') as f:
            f.write("<Bot>: Thank you. Bye!") #prints to current session's file
        f.close()
        print("<Bot>: Thank you. Bye!") #prints to console
        with open("../data/output.txt", "a") as g: #opens filewriter
            g.write("\nThank you. Bye! (This file will be overwritten when the program is started up again.)") #writes to filewriter
        g.close() #closes filewriter
        return True #returns true
    else:
        with open(currentSession, 'a') as f:
            f.write("<Bot>: I'm sorry. I did not understand the question. I will ask again.\n") #writes to current session's file
        f.close()
        print("<Bot>: I'm sorry. I did not understand the question. I will ask again.") #prints statement to console
    return False #returns false

def handleChitChat(q, currentSession):
    #makes a list of chit chat questions
    chitchatq = ["HELLO", "HI","HEY", "HOW ARE YOU", "WHAT'S THE WEATHER LIKE", "HOW WAS YOUR WEEKEND", "WHAT's UP", "UP"]
    #makes a list of answers to the questions
    chitchata = ["Hello.", "Hi.","Hey.", "I'm doing great.", "It seems to be sunny over here.", "My weekend was amazing.", "Nothing brotha.", "Nothing brotha"]
    highestRatio = -1000 #sets highestRatio to be negative
    index = 0 #sets default index to 0
    for x in chitchatq: #iterates through the list of chit chat questions
        ratio = fuzz.ratio(q, x) #uses the string matching algorithm built into fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio is higher than highestRatio
            highestRatio = ratio #sets the value of highestRatio to ratio
            index = chitchatq.index(x) #sets the value of index to the current index value of the list
    if (highestRatio > 55): #if the highestRatio is greater than 55
        with open(currentSession, 'a') as f:
            f.write("<Bot>: "+chitchata[index]) #writes to the current session's file
        f.close()
        print("<Bot>: "+chitchata[index]) #prints the chitchat answer in the corresponding index
    else:
        return findIfQuit(q, currentSession) #calls the findIfQuit function
    return False #returns false

def checkParts(q, fileName, list, currentSession):
    highestMap = list[0] #sets default value to be the beginning of the list
    highestRatio = -1000 #sets the first ratio to be negative
    for x in list: #iterates through the list of Data objects
        ratio = fuzz.ratio(q, x.retMatchString()) #finds the ratio using a word search algorithm from the library fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio just found is higher than the highestRatio variable
            highestRatio = ratio #sets the value of highestRatio to be ratio
            highestMap = x #sets the highestMap object to be the current object
    if (highestRatio > 55): #checks if the highest ratio is over 55
        print("<Bot>: Answer found. It is stored in the output.txt file in the data folder.") #tells user that answer has been found
        with open(currentSession, 'a') as f:
            f.write("<Bot>: Answer found. It is stored in the output.txt file in the data folder.") #writes to the current session's file
        f.close()
        with open("../data/output.txt", "a") as g: #opens filewriter
            g.write("\nAnswer:\n") #prints this line to the file
        g.close() #closes filewriter
        highestMap.printString(fileName) #calls the function from Data.py to print to file
    else:
        return handleChitChat(q, currentSession) #calls the handleChitChat function
    return False #returns false


# removeFillerWords(q) function is made by Anish Ghana and I have repurposed this function for my own chat bot
def removeFillerWords(q): #this function is supposed to remove common words to help with the string matching
    # Add all words that need to be removed from user input to an array
    words_to_remove = ["?", ".", "PROVIDE", "SHOW", "WHAT", "WHO", "THE", "IS", "OF", "ARE", "FOR", "ITEM", "TELL", "ME", "GIVE", "A", "AMD", "NVIDIA"]
    # get all words that doesn't have removed words
    resultwords = [word for word in re.split("\W+", q) if word not in words_to_remove]
    # join words together
    ret = ' '.join(resultwords)
    # return joined words
    return ret

def summaryCheck(q, currentSession):
    checks = ["SUMMARY", "SHOW CHAT SUMMARY", "CHAT SESSION"] #these are the phrases that are checked with
    highestRatio = -1000 #sets highestRatio to be negative
    index = 0 #sets default index to 0
    for x in checks: #iterates through the list of chit chat questions
        ratio = fuzz.ratio(q, x) #uses the string matching algorithm built into fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio is higher than highestRatio
            highestRatio = ratio #sets the value of highestRatio to ratio
            index = checks.index(x) #sets the value of index to the current index value of the list
    if (highestRatio > 55): #if the highestRatio is greater than 55
        if (index == 0): 
            temp = sessionStatistics.fullStat() #sets temp to the return value of fullStat function in sessionStatistics.py
            print(temp) #prints to terminal
            with open(currentSession, 'a') as f:
                f.write(temp) #writes to current session's file
            f.close()
        elif (index == 1):
            fileNumber = re.findall(r'\d+',q) #finds the number in the query
            temp = sessionStatistics.summary(fileNumber[0]) #sets temp to the return value of summary function in sessionStatistics.py
            print(temp) #prints temp to terminal
            with open(currentSession, 'a') as f:
                f.write(temp) #writes to current session's file
            f.close()
        else:
            fileNumber = re.findall(r'\d+',q) #finds the number in the query
            temp = sessionStatistics.showchat(fileNumber[0]) #sets temp to the return value of showchat function in sessionStatistics.py
            print(temp) #prints to terminal
            with open(currentSession, 'a') as f:
                f.write(temp) #writes to current session's file
            f.close()
        return True #returns True

def findScope(q, currentSession):
    #makes a list to check if query is for statistics
    checks = ["COMPANIES SUPPORT", "INFO HAVE", "INFORMATION HAVE"]
    highestRatio = -1000 #sets highestRatio to be negative
    index = 0 #sets default index to 0
    for x in checks: #iterates through the list of chit chat questions
        ratio = fuzz.ratio(q, x) #uses the string matching algorithm built into fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio is higher than highestRatio
            highestRatio = ratio #sets the value of highestRatio to ratio
            index = checks.index(x) #sets the value of index to the current index value of the list
    if (highestRatio > 55): #if the highestRatio is greater than 55
        if (index == 0): 
            print("<Bot>: I support queries about AMD and NVIDIA.") #prints to terminal
            with open(currentSession, 'a') as f:
                f.write("<Bot>: I support queries about AMD and NVIDIA.") #writes to current session's file
            f.close()
        elif (index == 1 or index == 2):
            print("<Bot>: I have information about parts 1-4 and items 1, 1A, 2, 3, 4, 5, 7, 7A, 8, 9, 9A, 9B, 9C, 10, 11, 12, 13, 14, 15.") #prints to terminal
            with open(currentSession, 'a') as f:
                f.write("<Bot>: I have information about parts 1-4 and items 1, 1A, 2, 3, 4, 5, 7, 7A, 8, 9, 9A, 9B, 9C, 10, 11, 12, 13, 14, 15.")
                #writes to current session's file
            f.close()
        return True #returns true
    

def mapQuery(q, fileName, list, currentSession):
    q = removeFillerWords(q) #calls function to remove filler words 
    check1 = summaryCheck(q, currentSession) #calls summary check function to see if query is asking about statistics
    if (check1): #if summaryCheck thinks that the query is about statistics, returns false 
        return False 
    check2 = findScope(q, currentSession) #calls findScope function to see if query is asking about scope of the chat bot
    if (check2): #if findScope thinks that the query is about the scope, returns false
        return False
    return checkParts(q, fileName, list, currentSession) #calls and returns the checkParts function (maps the query to a part, item, chitchat, or quit) 
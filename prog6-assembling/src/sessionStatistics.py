import csv

def summary(n): #prints the summary of a single chat session
    count = 0 #creates a variable named count and sets it to 0
    temp = ""
    with open("../data/chat_statistics.csv") as f: #opens the csv file
        csvReader = csv.reader(f) #creates a csv file reader
        for line in csvReader: #loops through each line in the csv
            count += 1 #incremets count by 1
            if (line[0] == str(n)): #checks to see if the session number in the csv file and compares it to the input value
                #prints the statement below
                temp = ("<Bot>: Chat "+str(n)+" has user asking "+line[2]+" times and system respond "+line[3]+" times. Total duration is "+line[4]+" seconds.")
    if (int(n)>=count): #checks to see if the value of input value is greater than or equal to the value of count
        #prints the statement below
        temp = ("<Bot>: Error. There are only "+str(count)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(count-1)+".")
    f.close() #closes the file
    return temp

def showchat(n): #prints the entire chat to the terminal
    fileName = "" #creates a fileName variable
    count = 0 #creates a variable named count and sets it to 0
    with open("../data/chat_statistics.csv") as f: #opens the csv file
        csvReader = csv.reader(f) #creates a csv file reader
        for line in csvReader: #goes through each line in the csv
            if (line[0] == n): #checks to see if the session number in the csv file and compares it to the input value
                fileName = line[1] #sets the fileName variable to the chat file variable in the csv file
            count+=1 #increments count by one
    f.close() #closes the file
    if (int(n)>=count): #checks to see if the input value is greater than or equal to the value of count
        #prints the statement below
        return ("<Bot>: Error. There are only "+str(count)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(count-1)+".") #returns so that the rest of the program does not run
    temp = "<Bot>: "
    temp += "Chat "+n+" chat is: \n" #prints this statement
    with open("../data/chat_sessions/"+fileName) as f: #opens a file reader for the correct chat session file
        for line in f: #iterates through the file
            temp += line + "\n" #prints the line
    f.close() #closes file reader
    return temp

def fullStat(): #finds the full statistics of the csv file
    #creates local variables
    totalNum = 0 
    totalUserUtt = 0
    totalSysUtt = 0
    totalTime = 0
    with open("../data/chat_statistics.csv") as f:
        csvReader = csv.reader(f) #opens the csv
        for line in csvReader: #reads line by line
            #increments variables
            totalNum += 1 
            totalUserUtt += int(line[2])
            totalSysUtt += int(line[3])
            totalTime += float(line[4])
    
    #returns this statement
    return "<Bot>: There are "+str(totalNum)+" chats to date with user asking "+str(totalUserUtt)+" times and system respond "+str(totalSysUtt)+" times. Total duration is "+str(totalTime)+" seconds."

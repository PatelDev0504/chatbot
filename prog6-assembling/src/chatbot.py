import initializer
import time
import QueryInterpreter

fileName = "../data/NVIDIA-10K-2024.txt" #NVIDIA is set to be the default company
exit = False #set exit variable to false

def findCompany(que):
    if (que.find("AMD") != -1): #checks to see if the substring "AMD" exists in the question
        return "../data/AMD-10K-2024.txt" #returns the file path for the AMD 10-K
    elif (que.find("NVIDIA") != -1): #checks to see if the substring "NVIDIA" exists in the question
        return "../data/NVIDIA-10K-2024.txt" #returns the file path for the NVIDIA 10-K

start_time = time.time() #start time
list = initializer.initEverything() #calls function in initializer.py
with open("../data/output.txt", "w") as g:
    g.write("Hello, this is the archive of the conversation.\n") #prints this line to the output file; removes everything inside it before
g.close()
currentSession = "../data/chat_sessions/session_"+str(time.time())+".txt" #creates the name of the current session's file
with open(currentSession, 'x') as f: 
    f.write("<Bot>: Welcome!\n") #creates the current session's file and prints to it
f.close()
print("<Bot>: Welcome!") #prints to terminal
while (not exit): #while loop so the program does not end after one iteration
    choice = input("<Bot>: Please enter a question that you have about amd or nvidia or enter Quit, quit, or q to exit the program.\n<User>: ") #prompts the user
    with open(currentSession, 'a') as f:
        f.write("<Bot>: Please enter a question that you have about amd or nvidia or enter Quit, quit, or q to exit the program.\n<User>: "+choice+"\n") #prints to current session's file
    f.close()
    with open("../data/output.txt", "a") as g: #opens filewriter
        g.write("\nQuestion: "+choice+"\n") #prints this line to the file
    g.close() #closes filewriter
    choice = choice.upper() #makes the user's input to be all upper case
    if (choice.find("AMD") != -1 or choice.find("NVIDIA") != -1): #checks to see if company name is mentioned in the user input
        fileName = findCompany(choice) #calling the findCompany function and setting the return value to the global variable fileName
    exit = QueryInterpreter.mapQuery(choice, fileName, list, currentSession) #sets exit equal to a function in QueryInterpreter.py
    

totalTime = "This program took %s seconds." % (time.time()-start_time) #finds the total time the program took
print(totalTime) #prints to terminal
with open(currentSession, 'a') as f:
    f.write("\n"+totalTime) #prints to current session's file
f.close()

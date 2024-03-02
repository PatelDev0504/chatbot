import Data #imports the class file

#created the variables fileName and exit to be used throughout the entire program 
fileName = "../data/NVIDIA_1-29-23.txt" #default company is NVIDIA
exit = False
list = []
#searches through the question given by the user to find the instance of "AMD" or "NVIDIA" and returns
#the file path
#if the company is not found, it prompts the user one time to enter the name of the company and then
#return the file path
def findCompany(que):
    if (que.find("AMD") != -1): #checks to see if the substring "AMD" exists in the question
        return "../data/AMD_12-30-23.txt" #returns the file path for the AMD 10-K
    elif (que.find("NVIDIA") != -1): #checks to see if the substring "NVIDIA" exists in the question
        return "../data/NVIDIA_1-29-23.txt" #returns the file path for the NVIDIA 10-K

def initData(): #creates all the data objects and stores them to a list
    list.append(Data.Data("ALL INFORMATION", "Table\sof\sContents", "SIGNATURES"))
    list.append(Data.Data("TELL ME EVERYTHING", "Table\sof\sContents", "SIGNATURES"))
    list.append(Data.Data("FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("ITEM 8", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("FINANCIAL STATEMENTS", "PART\sIV\s", "SIGNATURES"))
    list.append(Data.Data("PART 4", "PART\sIV\s", "SIGNATURES"))  
    list.append(Data.Data("COMPANY STRUCTURE", "PART\sIII", "PART\sIV"))
    list.append(Data.Data("PART 3", "PART\sIII", "PART\sIV")) 
    list.append(Data.Data("OPERATIONS AND DISCLOSURES", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("PART 2", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("BUSINESS BACKGROUND AND RISKS", "PART\sI\s", "PART\sII"))
    list.append(Data.Data("PART 1", "PART\sI\s", "PART\sII"))  
    list.append(Data.Data("BUSINESS", "ITEM\s1\.\s", "ITEM\s1A\.\s"))
    list.append(Data.Data("ITEM 1", "ITEM\s1\.\s", "ITEM\s1A\.\s"))  
    list.append(Data.Data("RISK FACTORS", "ITEM\s1A\.\s", "ITEM\s1B\.\s"))
    list.append(Data.Data("ITEM 1A", "ITEM\s1A\.\s", "ITEM\s1B\.\s"))  
    list.append(Data.Data("PROPERTIES", "ITEM\s2\.\s", "ITEM\s3\.\s"))
    list.append(Data.Data("ITEM 2", "ITEM\s2\.\s", "ITEM\s3\.\s"))
    list.append(Data.Data("LEGAL PROCEEDINGS", "ITEM\s3\.\s", "ITEM\s4\.\s"))
    list.append(Data.Data("ITEM 3", "ITEM\s3\.\s", "ITEM\s4\.\s"))
    list.append(Data.Data("MINE SAFETY DISCLOSURES", "ITEM\s4\.\s", "PART\sII"))
    list.append(Data.Data("ITEM 4", "ITEM\s4\.\s", "PART\sII"))
    list.append(Data.Data("MARKET FOR REGISTRANT’S COMMON EQUITY, RELATED STOCKHOLDER MATTERS AND ISSUER PURCHASES OF EQUITY SECURITIES", "ITEM\s5\.\s", "ITEM\s6\.\s"))
    list.append(Data.Data("ITEM 5", "ITEM\s5\.\s", "ITEM\s6\.\s"))
    list.append(Data.Data("MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS", "ITEM\s7\.\s", "ITEM\s7A\.\s"))
    list.append(Data.Data("ITEM 7", "ITEM\s7\.\s", "ITEM\s7A\.\s"))
    list.append(Data.Data("QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "ITEM\s7A\.\s", "ITEM\s8\.\s"))
    list.append(Data.Data("ITEM 7A", "ITEM\s7A\.\s", "ITEM\s8\.\s"))
    list.append(Data.Data("CHANGES IN AND DISAGREEMENTS WITH ACCOUNTANTS ON ACCOUNTING AND FINANCIAL DISCLOSURE", "ITEM\s9\.\s", "ITEM\s9A\.\s"))
    list.append(Data.Data("ITEM 9", "ITEM\s9\.\s", "ITEM\s9A\.\s"))
    list.append(Data.Data("CONTROLS AND PROCEDURES", "ITEM\s9A\.\s", "ITEM\s9B\.\s"))
    list.append(Data.Data("ITEM 9A", "ITEM\s9A\.\s", "ITEM\s9B\.\s"))
    list.append(Data.Data("OTHER INFORMATION", "ITEM\s9B\.\s", "ITEM\s9C\.\s"))
    list.append(Data.Data("ITEM 9B", "ITEM\s9B\.\s", "ITEM\s9C\.\s"))
    list.append(Data.Data("DISCLOSURE REGARDING FOREIGN JURISDICTIONS THAT PREVENT INSPECTIONS", "ITEM\s9C\.\s", "PART\sIII"))
    list.append(Data.Data("ITEM 9C", "ITEM\s9C\.\s", "PART\sIII"))
    list.append(Data.Data("DIRECTORS, EXECUTIVE OFFICERS AND CORPORATE GOVERNANCE", "ITEM\s10\.\s", "ITEM\s11\.\s"))
    list.append(Data.Data("ITEM 10", "ITEM\s10\.\s", "ITEM\s11\.\s"))
    list.append(Data.Data("EXECUTIVE COMPENSATION", "ITEM\s11\.\s", "ITEM\s12\.\s"))
    list.append(Data.Data("ITEM 11", "ITEM\s11\.\s", "ITEM\s12\.\s"))
    list.append(Data.Data("SECURITY OWNERSHIP OF CERTAIN BENEFICIAL OWNERS AND MANAGEMENT AND RELATED STOCKHOLDER MATTERS", "ITEM\s12\.\s", "ITEM\s13\.\s"))
    list.append(Data.Data("ITEM 12", "ITEM\s12\.\s", "ITEM\s13\.\s"))
    list.append(Data.Data("CERTAIN RELATIONSHIPS AND RELATED TRANSACTIONS, AND DIRECTOR INDEPENDENCE", "ITEM\s13\.\s", "ITEM\s14\.\s"))
    list.append(Data.Data("ITEM 13", "ITEM\s13\.\s", "ITEM\s14\.\s"))
    list.append(Data.Data("PRINCIPAL ACCOUNTANT FEES AND SERVICES", "ITEM\s14\.\s", "PART\sIV"))
    list.append(Data.Data("ITEM 14", "ITEM\s14\.\s", "PART\sIV"))
    list.append(Data.Data("EXHIBIT AND FINANCIAL STATEMENT SCHEDULES", "ITEM\s15\.\s", "ITEM\s16\.\s"))
    list.append(Data.Data("ITEM 15", "ITEM\s15\.\s", "ITEM\s16\.\s"))
    list.append(Data.Data("FORM 10-K SUMMARY", "ITEM\s16\.\s", "SIGNATURES"))
    list.append(Data.Data("ITEM 16", "ITEM\s16\.\s", "SIGNATURES"))


initData() #calls the function above
with open("../data/output.txt", "w") as g:
    g.write("Hello, this is the archive of the conversation.\n") #prints this line to the file
g.close()
while (not exit): #while loop so the program does not end after one iteration
    choice = input("<Bot>: Please enter a question that you have about amd or nvidia or enter Quit, quit, or q to exit the program.\n<User>: ") #prompts the user
    choice = choice.upper() #makes the user's input to be all upper case
    if (choice.find("AMD") != -1 or choice.find("NVIDIA") != -1): #checks to see if the input contained a company name
        fileName = findCompany(choice) #finds the company 10-K file by calling the findCompany function 
    if (choice == "QUIT" or choice == "Q"): #checks to see if the user wants to quit
        exit = True #changes the boolean value
        break #breaks the loop
    else:
        answerFound = False #sets the variable to false
        with open("../data/output.txt", "a") as g: #opens file writer
            g.write("\nQuestion: ") #writes to file
            g.write(choice) #writes the user input to the file
            if (fileName == "../data/AMD_12-30-23.txt"): #checks the company by using the filepath of the 10-K
                g.write("\nCompany Name: AMD\n") #writes company name to the file
            else:
                g.write("\nCompany Name: NVIDIA\n") #writes company name to the file; set as default
            g.write("\nAnswer:\n") #writes to the file
        g.close()
        for x in list: #iterates through the list of objects
            currentData = x.retName() #sets the name of the current object to currentData
            if (choice.find(currentData) != -1): #checks to see if the user input included the name of the current object
                x.printString(fileName) #calls the printString function in Data.py
                answerFound = True #sets the variable to true
        if (not answerFound): #if answerFound is false, then it prints "I could not find an answer"
            with open("../data/output.txt", "a") as g:
                print("<Bot>: I could not find an answer.")
                g.write("I could not find an answer.\n")
            g.close()
        else: #if answerFound is true, then it prints the following statement.
            print("<Bot>: Answer found. It is stored in the output.txt file in the data folder.")
import Data #imports the class file
from fuzzywuzzy import fuzz #importing fuzz from fuzzbuzz


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
    list.append(Data.Data("ALL INFORMATION EVERYTHING","Everything", "(Table\sof\sContents|INDEX)", "SIGNATURES"))
    list.append(Data.Data("FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA REVENUE EQUITY STOCK","Financial Statements and Supplementary Data", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("8","Financial Statements and Supplementary Data", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("FINANCIAL STATEMENTS","Part 4", "PART\sIV\s", "S[Ii][Gg][Nn][Aa][Tt][Uu][Rr][Ee][Ss]"))
    list.append(Data.Data("PART 4","Part 4", "PART\sIV\s", "S[Ii][Gg][Nn][Aa][Tt][Uu][Rr][Ee][Ss]"))
    list.append(Data.Data("COMPANY STRUCTURE","Part 3", "PART\sIII", "PART\sIV"))
    list.append(Data.Data("PART 3","Part 3", "PART\sIII", "PART\sIV"))
    list.append(Data.Data("OPERATIONS AND DISCLOSURES","Part 2", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("PART 2","Part 2", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("BUSINESS BACKGROUND AND RISKS","Part 1", "PART\sI\s", "PART\sII"))
    list.append(Data.Data("PART 1","Part 1", "PART\sI\s", "PART\sII"))
    list.append(Data.Data("ABOUT","Part 1", "PART\sI\s", "PART\sII"))  
    list.append(Data.Data("BUSINESS OVERVIEW","Business", "ITEM\s1\.\s", "ITEM\s1A\.\s"))
    list.append(Data.Data("1","Business", "ITEM\s1\.\s", "ITEM\s1A\.\s"))
    list.append(Data.Data("RISK FACTORS","Risk Factors", "ITEM\s1A\.\s", "ITEM\s1B\.\s"))
    list.append(Data.Data("1A","Risk Factors", "ITEM\s1A\.\s", "ITEM\s1B\.\s"))
    list.append(Data.Data("PROPERTIES OWN","Properties", "ITEM\s2\.\s", "ITEM\s3\.\s"))
    list.append(Data.Data("2","Properties", "ITEM\s2\.\s", "ITEM\s3\.\s"))
    list.append(Data.Data("LEGAL PROCEEDINGS","Legal Proceedings", "ITEM\s3\.\s", "ITEM\s4\.\s"))
    list.append(Data.Data("3","Legal Proceedings", "ITEM\s3\.\s", "ITEM\s4\.\s"))
    list.append(Data.Data("MINE SAFETY DISCLOSURES","Mine Safety Disclosures", "ITEM\s4\.\s", "PART\sII"))
    list.append(Data.Data("4","Mine Safety Disclosures", "ITEM\s4\.\s", "PART\sII"))
    list.append(Data.Data("MARKET REGISTRANT COMMON EQUITY RELATED STOCKHOLDER MATTERS AND ISSUER PURCHASES EQUITY SECURITIES","Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities", "ITEM\s5\.\s", "ITEM\s6\.\s"))
    list.append(Data.Data("5","Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities", "ITEM\s5\.\s", "ITEM\s6\.\s"))
    list.append(Data.Data("MANAGEMENT DISCUSSION AND ANALYSIS FINANCIAL CONDITION AND RESULTS OPERATIONS","Management’s Discussion and Analysis of Financial Condition and Results of Operations", "ITEM\s7\.\s", "ITEM\s7A\.\s"))
    list.append(Data.Data("7","Management’s Discussion and Analysis of Financial Condition and Results of Operations", "ITEM\s7\.\s", "ITEM\s7A\.\s"))
    list.append(Data.Data("QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK","Quantitative and Qualitative Disclosure About Market Risk", "ITEM\s7A\.\s", "ITEM\s8\.\s"))
    list.append(Data.Data("7A","Quantitative and Qualitative Disclosure About Market Risk", "ITEM\s7A\.\s", "ITEM\s8\.\s"))
    list.append(Data.Data("CHANGES IN AND DISAGREEMENTS WITH ACCOUNTANTS ON ACCOUNTING AND FINANCIAL DISCLOSURE","Changes in and Disagreements with Accountants on Accounting and Financial Disclosure", "ITEM\s9\.\s", "ITEM\s9A\.\s"))
    list.append(Data.Data("9","Changes in and Disagreements with Accountants on Accounting and Financial Disclosure", "ITEM\s9\.\s", "ITEM\s9A\.\s"))
    list.append(Data.Data("CONTROLS AND PROCEDURES","Controls and Procedures", "ITEM\s9A\.\s", "ITEM\s9B\.\s"))
    list.append(Data.Data("9A","Controls and Procedures", "ITEM\s9A\.\s", "ITEM\s9B\.\s"))
    list.append(Data.Data("ADDITIONAL MORE OTHER INFORMATION","Other Information", "ITEM\s9B\.\s", "ITEM\s9C\.\s"))
    list.append(Data.Data("9B","Other Information", "ITEM\s9B\.\s", "ITEM\s9C\.\s"))
    list.append(Data.Data("DISCLOSURE REGARDING FOREIGN JURISDICTIONS THAT PREVENT INSPECTIONS","Disclosures Regarding Foreign Jurisdictions that Prevent Inspections", "ITEM\s9C\.\s", "PART\sIII"))
    list.append(Data.Data("9C","Disclosures Regarding Foreign Jurisdictions that Prevent Inspections", "ITEM\s9C\.\s", "PART\sIII"))
    list.append(Data.Data("DIRECTORS EXECUTIVE OFFICERS AND CORPORATE GOVERNANCE","Directors, Executive Officers and Corporate Governance", "ITEM\s10\.\s", "ITEM\s11\.\s"))
    list.append(Data.Data("10","Directors, Executive Officers and Corporate Governance", "ITEM\s10\.\s", "ITEM\s11\.\s"))
    list.append(Data.Data("EXECUTIVE COMPENSATION DIRECTORS OFFICERS","Executive Compensation", "ITEM\s11\.\s", "ITEM\s12\.\s"))
    list.append(Data.Data("11","Executive Compensation", "ITEM\s11\.\s", "ITEM\s12\.\s"))
    list.append(Data.Data("SECURITY OWNERSHIP CERTAIN BENEFICIAL OWNERS AND MANAGEMENT AND RELATED STOCKHOLDER MATTERS","Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters", "ITEM\s12\.\s", "ITEM\s13\.\s"))
    list.append(Data.Data("12","Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters", "ITEM\s12\.\s", "ITEM\s13\.\s"))
    list.append(Data.Data("CERTAIN RELATIONSHIPS AND RELATED TRANSACTIONS AND DIRECTOR INDEPENDENCE","Certain Relationships and Related Transactions and Director Independence", "ITEM\s13\.\s", "ITEM\s14\.\s"))
    list.append(Data.Data("13","Certain Relationships and Related Transactions and Director Independence", "ITEM\s13\.\s", "ITEM\s14\.\s"))
    list.append(Data.Data("PRINCIPAL ACCOUNTANT FEES AND SERVICES","Principal Accountant Fees and Services", "ITEM\s14\.\s", "PART\sIV"))
    list.append(Data.Data("14","Principal Accountant Fees and Services", "ITEM\s14\.\s", "PART\sIV"))
    list.append(Data.Data("EXHIBIT AND FINANCIAL STATEMENT SCHEDULES","Exhibits and Financial Statement Schedules", "ITEM\s15\.\s", "ITEM\s16\.\s"))
    list.append(Data.Data("15","Exhibits and Financial Statement Schedules", "ITEM\s15\.\s", "ITEM\s16\.\s"))
    list.append(Data.Data("FORM 10-K SUMMARY","Form 10-K Summary", "ITEM\s16\.\s", "SIGNATURES"))
    list.append(Data.Data("16","Form 10-K Summary", "ITEM\s16\.\s", "SIGNATURES"))


def findIfQuit(q):
    #creates a list of quit prompts
    quitPrompts = ["QUIT", "LEAVE", "GO AWAY", "STOP", "EXIT", "Q", "BYE"]
    highestRatio = -1000 #sets highestRatio to be negative
    for x in quitPrompts: #iterates through the list
        ratio = fuzz.partial_ratio(x, q) #uses a string matching algorithm from fuzzywuzzy 
        if (ratio > highestRatio): #checks to see if the ratio is greater than highestRatio
            highestRatio = ratio #sets the highestRatio to ratio
    if (highestRatio >= 90): #checks to see if highestRatio is greater than or equal to 90
        print("<Bot>: Thank you. Bye!") #prints to console
        with open("../data/output.txt", "a") as g: #opens filewriter
            g.write("<Bot>: Thank you. Bye!") #writes to filewriter
        g.close() #closes filewriter
        return True #returns true
    else:
        print("<Bot>: I'm sorry. I did not understand the question. I will ask again.") #prints statement to console
    return False #returns false

def handleChitChat(q):
    #makes a list of chit chat questions
    chitchatq = ["HELLO", "HI", "HOW ARE YOU", "WHAT'S THE WEATHER LIKE", "HOW WAS YOUR WEEKEND", "WHAT's UP", "UP"]
    #makes a list of answers to the questions
    chitchata = ["Hello.", "Hi.", "I'm doing great.", "It seems to be sunny over here.", "My weekend was amazing.", "Nothing brotha.", "Nothing brotha"]
    highestRatio = -1000 #sets highestRatio to be negative
    index = 0 #sets default index to 0
    for x in chitchatq: #iterates through the list of chit chat questions
        ratio = fuzz.ratio(q, x) #uses the string matching algorithm built into fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio is higher than highestRatio
            highestRatio = ratio #sets the value of highestRatio to ratio
            index = chitchatq.index(x) #sets the value of index to the current index value of the list
    if (highestRatio > 55): #if the highestRatio is greater than 55
        print("<Bot>: "+chitchata[index]) #prints the chitchat answer in the corresponding index
    else:
        return findIfQuit(q) #calls the findIfQuit function
    return False #returns false

def mapQuery(q):
    highestMap = list[0] #sets default value to be the beginning of the list
    highestRatio = -1000 #sets the first ratio to be negative
    for x in list: #iterates through the list of Data objects
        ratio = fuzz.ratio(q, x.retMatchString()) #finds the ratio using a word search algorithm from the library fuzzywuzzy
        if (ratio > highestRatio): #checks to see if the ratio just found is higher than the highestRatio variable
            highestRatio = ratio #sets the value of highestRatio to be ratio
            highestMap = x #sets the highestMap object to be the current object
    if (highestRatio > 55): #checks if the highest ratio is over 55
        print("<Bot>: I am assuming that you want to find information about "+highestMap.retName()+" because the ratio from mapping is ") #prints the assumption that the chat bot is making
        print(highestRatio) #prints the ratio
        print("<Bot>: Answer found. It is stored in the output.txt file in the data folder.") #tells user that answer has been found
        with open("../data/output.txt", "a") as g: #opens filewriter
            g.write("\nAnswer:\n") #prints this line to the file
        g.close() #closes filewriter
        highestMap.printString(fileName) #calls the function from Data.py to print to file
    else:
        return handleChitChat(q) #calls the handleChitChat function
    return False #returns false

def removeFillerWords(word): #this function is supposed to remove common words to help with the string matching
    if (word.find("?") != -1): #checks for a question mark at the end of the question
        word = word[:(len(word)-1)] #removes the question mark from word
    split = word.split(" ") #splits word into a list of strings
    if "WHAT" in split: #checks to see if "what" is contained in the list
        split.remove("WHAT") #removes instances of what from the list
    if "THE" in split: #checks to see if "the" is contained in the list
        split.remove("THE") #removes instances of the from the list
    if "IS" in split: #checks to see if "is" is contained in the list
        split.remove("IS") #removes instances of is from the list
    if "AMD" in split: #checks to see if "amd" is contained in the list
        split.remove("AMD") #removes instances of amd from the list
    if "NVIDIA" in split: #checks to see if "nvidia" is contained in the list
        split.remove("NVIDIA") #removes instances of nvidia from the list
    if "OF" in split: #checks to see if "of" is contained in the list
        split.remove("OF") #removes instances of of from the list
    if "ARE" in split: #checks to see if "are" is contained in the list
        split.remove("ARE") #removes instances of are from the list
    if "FOR" in split: #checks to see if "for" is contained in the list
        split.remove("FOR") #removes instances of for from the list
    if "ITEM" in split: #checks to see if "item" is contained in the list
        split.remove("ITEM") #removes instances of item from the list
    if "TELL" in split: #checks to see if "tell" is contained in the list
        split.remove("TELL") #removes instances of tell from the list
    if "ME" in split:#checks to see if "me" is contained in the list
        split.remove("ME") #removes instances of me from the list
    if "GIVE" in split: #checks to see if "give" is contained in the list
        split.remove("GIVE") #removes instances of give from the list
    if "A" in split: #checks to see if "a" is contained in the list
        split.remove("A") #removes instances of a from the list
    ret = "" #creates a string that will be returned
    for x in split: #goes through every item remaining in the list
        ret += x + " " #concatonates the items
    return ret #returns ret


initData() #calls the function above
with open("../data/output.txt", "w") as g:
    g.write("Hello, this is the archive of the conversation.\n") #prints this line to the file
g.close()
print("<Bot>: Welcome!")
while (not exit): #while loop so the program does not end after one iteration
    choice = input("<Bot>: Please enter a question that you have about amd or nvidia or enter Quit, quit, or q to exit the program.\n<User>: ") #prompts the user
    with open("../data/output.txt", "a") as g: #opens filewriter
        g.write("\nQuestion: "+choice+"\n") #prints this line to the file
    g.close() #closes filewriter
    choice = choice.upper() #makes the user's input to be all upper case
    if (choice.find("AMD") != -1 or choice.find("NVIDIA") != -1): #checks to see if company name is mentioned in the user input
        fileName = findCompany(choice) #calling the findCompany function and setting the return value to the global variable fileName
    choice = removeFillerWords(choice) #calls the removeFillerWords function and setting it equal to choice
    exit = mapQuery(choice) #sets exit to the return value of the mapQuery function

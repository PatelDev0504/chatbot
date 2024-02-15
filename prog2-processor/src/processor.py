#imported the regular expression library
import re

#created the variables fileName and exit to be used throughout the entire program 
fileName = ""
exit = False

#searches through the question given by the user to find the instance of "AMD" or "NVIDIA" and returns
#the file path
#if the company is not found, it prompts the user one time to enter the name of the company and then
#return the file path
def findCompany(que):
    if (que.find("AMD") != -1): #checks to see if the substring "AMD" exists in the question
        return "../data/AMD_12-30-23.txt" #returns the file path for the AMD 10-K
    
    elif (que.find("NVIDIA") != -1): #checks to see if the substring "NVIDIA" exists in the question
        return "../data/NVIDIA_1-29-23.txt" #returns the file path for the NVIDIA 10-K
    
    else:
        #prompts the user to enter the company name
        companyName=input("I'm sorry, but I did not get the company name. Can you please tell me which company you are referring to?")
        companyName = companyName.upper() 
        if (companyName.find("AMD") != -1): #checks to see if the substring "AMD" exists in the question
            return "../data/AMD_12-30-23.txt" #returns the file path for the AMD 10-K
        
        elif (companyName.find("NVIDIA") != -1): #checks to see if the substring "NVIDIA" exists in the question
            return "../data/NVIDIA_1-29-23.txt" #returns the file path for the NVIDIA 10-K
        
        else: #prints a statement if the company name is not found and then asks the question again
            print("I'm sorry, but I still cannot understand the company. I will ask for the question again!")


#prints the lines in the file between the starting index and the ending index
def printResults(start, end):
    #initalizes the regular expression for the start
    regexStart = re.compile(start)
    #initalizes the regular expression for the end
    regexEnd = re.compile(end)
    #creates a boolean value to determine whether the file reader is inbetween the start and end
    isWithin = False
    with open(fileName, "r") as f: #opens the file reader
        with open("../data/output.txt", "w") as g: #opens the file writer
            for line_i, line in enumerate(f, 1): #iterating through the file one line at a time
                if regexStart.search( line ): #checking the line to see if the start regex is contained within it
                    isWithin = True #changes the boolean value to true
                if regexEnd.search( line ): #checking the line to see if the end regex is contained within it
                        isWithin = False #changes the boolean value to be false again
                if (isWithin): #checks the boolean value to ensure that the file reader is between the start and end regex
                    g.write(line) #prints the line to the output file
    f.close() #closes the file reader
    g.close() #closes the file writer
    print("The output will be erased when another question is asked. When you are ready ask your question.")
    
#searches the question to determine if the question contains the certain phrase referencing a part of the 10-K files
def findSection(que):
    if (que.find("ALL INFORMATION") != -1): #checks if the user wants all the information
        #calls the printResults function with the start and end regex to give all the information within the file
        printResults("Table\sof\sContents", "SIGNATURES") 
        #checks if the user wants item 8
    elif (que.find("FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA") != -1):
        #calls the printResults function with the start and end regex to give item 8 within the file
        printResults("ITEM\s8\.\s", "ITEM\s9\.\s")
        #checks if the user wants part 4
    elif (que.find("FINANCIAL STATEMENTS")!= -1):
        #calls the printResults function with the start and end regex to give part 4 within the file
        printResults("PART\sIV\s", "SIGNATURES")
        #checks if the user wants part 3
    elif (que.find("COMPANY STRUCTURE")!= -1):
        #calls the printResults function with the start and end regex to give part 3 within the file
        printResults("PART\sIII", "PART\sIV")
        #checks if the user wants part 2
    elif (que.find("OPERATIONS AND DISCLOSURES") != -1):
        #calls the printResults function with the start and end regex to give part 2 within the file
        printResults("PART\sII", "PART\sIII")
        #checks if the user wants part 1
    elif (que.find("BUSINESS BACKGROUND AND RISKS") != -1):
        #calls the printResults function with the start and end regex to part 1 within the file
        printResults("PART\sI\s", "PART\sII")
        #checks if the user wants item 1
    elif (que.find("BUSINESS") != -1):
        #calls the printResults function with the start and end regex to give item 1 within the file
        printResults("ITEM\s1\.\s", "ITEM\s1A\.\s")
        #checks if the user wants item 1A
    elif (que.find("RISK FACTORS") != -1):
        #calls the printResults function with the start and end regex to give item 1a within the file
        printResults("ITEM\s1A\.\s", "ITEM\s1B\.\s")
        #checks if the user wants item 1B
    elif (que.find("UNRESOLVED STAFF COMMENTS") != -1):
        #checks to see if the company is amd or nvidia because the 10-K for AMD includes an additional section compared to NVIDIA
        if (fileName.find("/data/AMD_12-30-23.txt") != -1):
            #calls the printResults function with the start and end regex to give item 1b for amd's file
            printResults("ITEM\s1B\.\s", "ITEM\s1C\.\s")
        elif (fileName.find("/data/NVIDIA_1-29-23.txt") != -1):
            #calls the printResults function with the start and end regex to give item 1b for nvidia's file
            printResults("ITEM\s1B\.\s", "ITEM\s2\.\s")
        #checks if the user wants item 2
    elif (que.find("PROPERTIES") != -1):
        #calls the printResults function with the start and end regex to give item 2 within the file
        printResults("ITEM\s2\.\s", "ITEM\s3\.\s")
        #checks if the user wants item 3
    elif (que.find("LEGAL PROCEEDINGS") != -1):
        #calls the printResults function with the start and end regex to give item 3 within the file
        printResults("ITEM\s3\.\s", "ITEM\s4\.\s")
        #checks if the user wants item 4
    elif (que.find("MINE SAFETY DISCLOSURES") != -1):
        #calls the printResults function with the start and end regex to give item 4 within the file
        printResults("ITEM\s4\.\s", "PART\sII")
        #checks if the user wants item 5
    elif (que.find("MARKET FOR REGISTRANT’S COMMON EQUITY, RELATED STOCKHOLDER MATTERS AND ISSUER PURCHASES OF EQUITY SECURITIES") != -1):
        #calls the printResults function with the start and end regex to give item 5 within the file
        printResults("ITEM\s5\.\s", "ITEM\s6\.\s")
        #checks if the user wants item 7
    elif (que.find("MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS") != -1):
        #calls the printResults function with the start and end regex to give item 7 within the file
        printResults("ITEM\s7\.\s", "ITEM\s7A\.\s")
        #checks if the user wants item 7A
    elif (que.find("QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK") != -1):
        #calls the printResults function with the start and end regex to give item 7A within the file
        printResults("ITEM\s7A\.\s", "ITEM\s8\.\s")
        #checks if the user wants item 9
    elif (que.find("CHANGES IN AND DISAGREEMENTS WITH ACCOUNTANTS ON ACCOUNTING AND FINANCIAL DISCLOSURE") != -1):
        #calls the printResults function with the start and end regex to give item 9 within the file
        printResults("ITEM\s9\.\s", "ITEM\s9A\.\s")
        #checks if the user wants item 9A
    elif (que.find("CONTROLS AND PROCEDURES") != -1):
        #calls the printResults function with the start and end regex to give item 9A within the file
        printResults("ITEM\s9A\.\s", "ITEM\s9B\.\s")
        #checks if the user wants item 9B
    elif (que.find("OTHER INFORMATION") != -1):
        #calls the printResults function with the start and end regex to give item 9B within the file
        printResults("ITEM\s9B\.\s", "ITEM\s9C\.\s")
        #checks if the user wants item 9C
    elif (que.find("DISCLOSURE REGARDING FOREIGN JURISDICTIONS THAT PREVENT INSPECTIONS") != -1):
        #calls the printResults function with the start and end regex to give item 9C within the file
        printResults("ITEM\s9C\.\s", "PART\sIII")
        #checks if the user wants item 10
    elif (que.find("DIRECTORS, EXECUTIVE OFFICERS AND CORPORATE GOVERNANCE") != -1):
        #calls the printResults function with the start and end regex to give item 10 within the file
        printResults("ITEM\s10\.\s", "ITEM\s11\.\s")
        #checks if the user wants item 11
    elif (que.find("EXECUTIVE COMPENSATION") != -1):
        #calls the printResults function with the start and end regex to give item 11 within the file
        printResults("ITEM\s11\.\s", "ITEM\s12\.\s")
        #checks if the user wants item 12
    elif (que.find("SECURITY OWNERSHIP OF CERTAIN BENEFICIAL OWNERS AND MANAGEMENT AND RELATED STOCKHOLDER MATTERS") != -1):
        #calls the printResults function with the start and end regex to give item 12 within the file
        printResults("ITEM\s12\.\s", "ITEM\s13\.\s")
        #checks if the user wants item 13
    elif (que.find("CERTAIN RELATIONSHIPS AND RELATED TRANSACTIONS, AND DIRECTOR INDEPENDENCE") != -1):
        #calls the printResults function with the start and end regex to give item 13 within the file
        printResults("ITEM\s13\.\s", "ITEM\s14\.\s")
        #checks if the user wants item 14
    elif (que.find("PRINCIPAL ACCOUNTANT FEES AND SERVICES") != -1):
        #calls the printResults function with the start and end regex to give item 14 within the file
        printResults("ITEM\s14\.\s", "PART\sIV")
        #checks if the user wants item 15
    elif (que.find("EXHIBIT AND FINANCIAL STATEMENT SCHEDULES") != -1):
        #calls the printResults function with the start and end regex to give item 15 within the file
        printResults("ITEM\s15\.\s", "ITEM\s16\.\s")
        #checks if the user wants item 16
    elif (que.find("FORM 10-K SUMMARY") != -1):
        #calls the printResults function with the start and end regex to give item 16 within the file
        printResults("ITEM\s16\.\s", "SIGNATURES")
    else:
        #prints a statement and returns to the question if none of the statements listed in the 
        # "text_output.txt" file were given
        print("I could not find any information. I will ask for another question now!")
    



#loops through the program until the user specifies otherwise
while (not exit):
    #prompts for the question 
    question=input("Please enter a question that you have about AMD or NVIDIA and please specify the company in the question or enter 1 to exit the program.")
    #if the user inputs "1", then the program is ended
    if (question == "1"):
        exit = True
        break
    #changes the question to be uppercase
    question = question.upper()
    #calls the findCompany function and sets the fileName equal to the value returned
    fileName = findCompany(question)
    #calls the findSection function
    findSection(question)

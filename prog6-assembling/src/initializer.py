import scraper
import Data
import csv 
import os 
import re 

def initCSV(): #creates the csv file with the chat session files
    list = [] #creates an empty list
    #creates the following 4 variables and sets them equal to 0
    for path in os.listdir('../data/chat_sessions'): #iterates through all the files in the chat_sessions folder
        list.append(path) #adds the file to the empty list
    with open("../data/chat_statistics.csv", 'w') as csvfile: #opens a filewriter for the csv writer
        writer = csv.writer(csvfile) #creates a csv writer using the csv library
        sessionNum = 0 #creates a variable called sessionNum and sets it to 0
        for x in list: #iterates through the list
            chatfile = x #creates a chatfile variable and sets it equal to the name of current file
            userUtt = 0 #creates a userUtt variable and sets it to 0
            sysUtt = 0 #creates a sysUtt variable and sets it to 0
            time = 0 #creates a time variable and sets it to 0
            with open("../data/chat_sessions/"+x, "r") as f: #opens a file reader for the current file
                for line_i, line in enumerate(f, 1): #iterates through each line in the file
                    bot = re.compile("<Bot>:") #creates a regex for the bot utterances
                    user = re.compile("<User>:") #creates a regex for the user utterances
                    if (bot.search(line)): #checks to see if the bot regex is in the line
                        sysUtt += 1 #increments the sysUtt by 1
                    elif (user.search(line)): #checks to see if the user regex is in the line
                        userUtt += 1 #increments the userUtt by 1
                    elif (line.find("seconds") != -1): #checks to see if the word seconds is in the line
                        end = line.find(" seconds") #finds the index of the word seconds
                        time = line[18:end] #sets time equal to the correct substring of the line
            writer.writerow([sessionNum, chatfile, userUtt, sysUtt, time]) #writes a row into the csv file
            sessionNum += 1 #increments the sessionNum by 1
    csvfile.close() #closes the filewriter

def initEverything():
    scraper.scrapeFile("AMD") #calls the scrapeFile function for amd in scraper.py
    scraper.scrapeFile("NVIDIA") #calls the scrapeFile function for nvidia in scraper.py
    initCSV() #calls the initCSV function above
    list = [] #creates empty list
    #creates Data objects and adds them to the list
    list.append(Data.Data("ALL INFORMATION","Everything", "(Table\sof\sContents|INDEX)", "SIGNATURES"))
    list.append(Data.Data("EVERYTHING","Everything", "(Table\sof\sContents|INDEX)", "SIGNATURES"))
    list.append(Data.Data("FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA REVENUE EQUITY STOCK","Financial Statements and Supplementary Data", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("8","Financial Statements and Supplementary Data", "ITEM\s8\.\s", "ITEM\s9\.\s"))
    list.append(Data.Data("FINANCIAL STATEMENTS","Part 4", "PART\sIV\s", "S[Ii][Gg][Nn][Aa][Tt][Uu][Rr][Ee][Ss]"))
    list.append(Data.Data("PART 4","Part 4", "PART\sIV\s", "S[Ii][Gg][Nn][Aa][Tt][Uu][Rr][Ee][Ss]"))
    list.append(Data.Data("COMPANY STRUCTURE","Part 3", "PART\sIII", "PART\sIV"))
    list.append(Data.Data("PART 3","Part 3", "PART\sIII", "PART\sIV"))
    list.append(Data.Data("OPERATIONS AND DISCLOSURES","Part 2", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("PART 2","Part 2", "PART\sII", "PART\sIII")) 
    list.append(Data.Data("BUSINESS BACKGROUND AND RISKS","Part 1", "PART\sI\n", "PART\sII"))
    list.append(Data.Data("PART 1","Part 1", "PART\sI\n", "PART\sII"))
    list.append(Data.Data("ABOUT","Part 1", "PART\sI\n", "PART\sII"))  
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
    list.append(Data.Data("CEO","Directors, Executive Officers and Corporate Governance", "ITEM\s10\.\s", "ITEM\s11\.\s"))
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
    
    return list #returns the list
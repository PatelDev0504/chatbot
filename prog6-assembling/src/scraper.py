from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

#I reused Tarun Ramkumar's PA1 to implement this method
#this function takes the website link and takes the content there and converts it to a useable txt file using a web scraper.
def scrapeFile(company):
    if(company == "AMD"):
        url = "https://www.sec.gov/Archives/edgar/data/2488/000000248824000012/amd-20231230.htm"
        file = open("../data/AMD-10K-2024.txt","w", encoding =  "utf-8")
    elif (company == "NVIDIA"):
        url = "https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm"
        file = open("../data/NVIDIA-10K-2024.txt","w", encoding =  "utf-8")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    website = requests.get(url = url, headers = headers)
    html = website.content.decode("utf-8")
    parser = BeautifulSoup(html,"html.parser")
    start = False
    headers = []
    for i in parser.stripped_strings:
        line = str(i)
        if "UNITED" in i and start == False:
            start = True
        if(start):
            #print(line)
            if(len(line) > 1):
                file.write(line+"\n")
    #print(headers)
    file.close()
from contentScraper import ContentScraper
import json

myScraper = ContentScraper()

def dataChecker(scrapedData):
    if (str(scrapedData) == "[]"):
        print("failed to find related info")
        return False
    else:
        return True
    

while True:
    usrURL = input("Paste a url: ")
    usrWants = [input(f"What would you like from {usrURL}? ")]
    
    myResult = myScraper.build(usrURL, usrWants)
    dataChecker(myResult)
     
    if dataChecker(myResult) == True:
        outputFile = open("corpusData/contentScraperDump.json", "a")
        json.dump(myResult, outputFile) # adds as a list but will need json formatting
        print("\n\ncontent added to json file\n\n")
from contentScraper import ContentScraper
import json

myScraper = ContentScraper()

def data_checker(scraped_data):
    if (str(scraped_data) == "[]"):
        print("failed to find related info")
        return False
    else:
        return True
    

while True:
    usrURL = input("Paste a url: ")
    usrWants = [input(f"What would you like from {usrURL}? ")]
    
    myResult = myScraper.build(usrURL, usrWants)
    data_checker(myResult)
     
    if data_checker(myResult) == True:
        outputFile = open("corpusData/contentScraperDump.json", "a")
        json.dump(myResult, outputFile) # adds as a list but will need json formatting
        print("\n\ncontent added to json file\n\n")
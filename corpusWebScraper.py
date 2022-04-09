from contentScraper import ContentScraper
import json

myScraper = ContentScraper()

def data_checker(scraped_data):
    if str(scraped_data) == "[]":
        print("failed to find related info")
        return False
    else:
        return True

def result_formatter(scraped_result):
    return scraped_result

while True:
    usrURL = input("Paste a url: ")
    usrWants = [input(f"What would you like from {usrURL}? ")]
    
    myResult = myScraper.build(usrURL, usrWants)
    data_checker(myResult)
     
    if data_checker(myResult) == True:
        outputFile = open("corpusData/contentScraperDump.json", "a")
        json.dump(result_formatter(myResult), outputFile, indent = 4, sort_keys=True)
        print("\n\ncontent added to json file\n\n")
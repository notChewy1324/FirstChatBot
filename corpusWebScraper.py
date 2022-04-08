from contentScraper import ContentScraper
import json

myScraper = ContentScraper()

while True:
    usrURL = input("Paste a url: ")
    usrWants = [input(f"What would you like from {usrURL}? ")]
    
    myResult = myScraper.build(usrURL, usrWants)
     
    outputFile = open("corpusData/contentScraperDump.json", "a")
    json.dump(myResult, outputFile) # adds as a list but will need json formatting
    print("\n\ncontent added to json file\n\n")
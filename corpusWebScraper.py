from contentScraper import ContentScraper
import json

myScraper = ContentScraper()

url = 'https://www.apple.com/'

wantedInfo = ["iPhone"]

myResult = myScraper.build(url, wantedInfo)

outputFile = open("corpusData/contentScraperDump.json", "w")
json.dump(myResult, outputFile)
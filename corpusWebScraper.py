from contentScraper import ContentScraper # Will use this as the local custom backend code instead of 3rd party pip

myScraper = ContentScraper()

testURL = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python' # instead of url make json file

wantedInfo = ["What are metaclasses in Python?"]

myResult = myScraper.build(testURL, wantedInfo)
print(myResult)
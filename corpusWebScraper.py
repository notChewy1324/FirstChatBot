from contentScraper import ContentScraper # Will use this as the local custom backend code instead of a 3rd party pip

myScraper = ContentScraper()

url = 'https://www.apple.com/'

wantedInfo = ["iPhone"]

myResult = myScraper.build(url, wantedInfo)
print(myResult) # will put into a json file for training use
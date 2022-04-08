from autoscraper import AutoScraper # from a pip install / will remove when un-needed

from contentScraper import ContentScraper # Will use this as the local custom backend code instead of 3rd party pip

scraper = AutoScraper()

url = 'corpusData/corupusTrain_test_2.json'

wantedInfo = []

result = scraper.build(url, wantedInfo)
print(result)
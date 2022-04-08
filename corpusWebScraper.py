from autoscraper import AutoScraper
scraper = AutoScraper()

url = 'corpusData/corupusTrain_test_2.json'

wantedInfo = []

result = scraper.build(url, wantedInfo)
print(result)
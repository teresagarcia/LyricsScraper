import scrapy

from scrapy.crawler import CrawlerProcess

BASE_SEARCH = "https://search.daum.net/search?w=tot&q="
query = "재중 햇살 좋은 날"

class DaumSpider(scrapy.Spider):
    name="daum"
    
    def start_requests(self):  
        full_search_url = BASE_SEARCH + query
        yield scrapy.Request(full_search_url, callback=self.parsehttp)

    def parsehttp(self, response):
        self.logger.info('Recieved response from {}'.format(response.url))
        print(response.body)

if __name__ == "__main__":
    process = CrawlerProcess()

    process.crawl(DaumSpider)
    process.start()

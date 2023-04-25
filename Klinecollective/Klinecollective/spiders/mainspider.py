import time
import scrapy

class MainspiderSpider(scrapy.Spider):
    start_time = time.time()
    name = "mainspider"
    allowed_domains = ["klinecollective.com"]
    start_urls = [
        "https://klinecollective.com/shop/"
    ]

    def parse(self, response):
        products = response.xpath("//div[3]/ul[@class='products columns-3']/li")
        if(products):
            for product in products:
                item = product.xpath("./div/a/@href").get()
                yield {"URL": item}
            nextPage = response.xpath("//nav/a[@class='next page-numbers']/@href").get()
            if nextPage is not None:
                nextPageURL = nextPage
                yield response.follow(nextPageURL, callback=self.parse)
        print("--- %s seconds ---" % round(time.time() - self.start_time, 3))
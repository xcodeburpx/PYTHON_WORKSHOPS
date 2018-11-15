import scrapy
from scrapy.loader import ItemLoader
from project_101_6.items import QuoteItem

class GoodReadsSpider(scrapy.Spider):

    # identity
    name="goodreads" # <- call spider from terminal

    # request <- initiate the request
    # def start_requests(self):
    #     # One URL address
    #     url = "https://www.goodreads.com/quotes?page=1"
    #
    #     # send the request
    #     # self.parse -> save the HTML markup
    #     yield scrapy.Request(url=url, callback=self.parse)

    # Shortcut <- default methods
    start_urls = [
        "https://www.goodreads.com/quotes?page=1"
    ]

    # response
    def parse(self, response):

        # Grab values with Xpath
        # ERROR: we didn't tell to execute this on current quote!
        # Fix -> . at the beginning of the xpath
        for quote in response.xpath("//div[@class='quote']"):

            #TODO:  Proper data formatting
            #TODO: Input and Output Processor
            loader = ItemLoader(item=QuoteItem(), selector=quote, response=response)
            loader.add_xpath('text',".//div[@class='quoteText']/text()[1]")
            loader.add_xpath('author',".//span[@class='authorOrTitle']")
            loader.add_xpath('tags',".//div[@class='greyText smallText left']/a")
            yield loader.load_item()


        # Grab 'next_page' href value
        next_page = response.xpath("//a[@class='next_page']/@href").extract_first()

        # Grab '/quotes?page=2'
        # TODO: settings.py
        # TODO: items.py
        # TODO: pipelines.py
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
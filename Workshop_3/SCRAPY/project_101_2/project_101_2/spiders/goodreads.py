import scrapy

class GoodReadsSpider(scrapy.Spider):

    # identity
    name="goodreads" # <- call spider from terminal

    # request <- initiate the request
    def start_requests(self):
        # One URL address
        url = "https://www.goodreads.com/quotes?page=1"

        # send the request
        # self.parse -> save the HTML markup
        yield scrapy.Request(url=url, callback=self.parse)

    # response
    def parse(self, response):

        # Grab values with Xpath
        # ERROR: we didn't tell to execute this on current quote!
        # Fix -> . at the beginning of the xpath
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'author': quote.xpath(".//span[@class='authorOrTitle']/text()").extract_first(),
                'tags': quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract()
            }

        # Grab 'next_page' href value
        next_page = response.selector.xpath("//a[@class='next_page']/@href").extract_first()

        # Grab '/quotes?page=2'
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
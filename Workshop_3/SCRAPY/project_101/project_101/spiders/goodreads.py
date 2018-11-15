import scrapy

class GoodReadsSpider(scrapy.Spider):

    # identity
    name="goodreads" # <- call spider from terminal

    # request <- initiate the request
    def start_requests(self):
        # Create the list of URLs
        urls = [
            "https://www.goodreads.com/quotes?page=1",
            "https://www.goodreads.com/quotes?page=2",
            "https://www.goodreads.com/quotes?page=3",
            "https://www.goodreads.com/quotes?page=4",
            "https://www.goodreads.com/quotes?page=5",
            "https://www.goodreads.com/quotes?page=6",
            "https://www.goodreads.com/quotes?page=7",
            "https://www.goodreads.com/quotes?page=8",
            "https://www.goodreads.com/quotes?page=9",
            "https://www.goodreads.com/quotes?page=10"
        ]

        for url in urls:
            # send the request
            # self.parse -> save the HTML markup
            yield scrapy.Request(url=url, callback=self.parse)

    # response
    def parse(self, response):

        # Grab the page number
        pagenumber = response.url.split("=")[1]
        _file = "{0}.html".format(pagenumber)

        # Save the response
        with open(_file, "wb") as f:
            f.write(response.body)
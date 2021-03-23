import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.logger.info('Hello, this is my first spider')
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall()
            }

        author_url = response.css('.author + a::attr(href)').get()
        self.logger.info('get author page')
        yield response.follow(author_url, callback=self.parse_author)

        for a in response.css('li.next a'):  # <class 'scrapy.selector.unified.SelectorList'>
            yield response.follow(a, callback=self.parse)  # <class 'scrapy.selector.unified.Selector'>

    def parse_author(self, response):
        yield {
            'author_name': response.css('.author-title::text').get(),
            'author_birthday': response.css('.author-born-date::text').get(),
            'author_bornlocation': response.css('.author-born-location::text').get(),
            'author_bio': response.css('.author-description::text').get()
        }
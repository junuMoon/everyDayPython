import scrapy
from tutorial.items import QuoteItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.logger.info(f'Parse function called on {response.url}')
        quotes = response.css('div.quote')

        for quote in quotes:
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css('quote_content', '.text::text')
            loader.add_css('tags', '.tag::text')
            
            quote_item = loader.load_item()
            author_url = quote.css('.author + a::attr(href)').get()

            yield response.follow(author_url,
                                 callback=self.parse_author,
                                 meta={'quote_item': quote_item})

        for a in response.css('li.next a'):  # <class 'scrapy.selector.unified.SelectorList'>
            yield response.follow(a, callback=self.parse)  # <class 'scrapy.selector.unified.Selector'>

    def parse_author(self, response):
        quote_item = response.meta['quote_item']
        loader = ItemLoader(item=quote_item, response=response)
        loader.add_css('author_name', '.author-title::text')
        loader.add_css('author_birthdate', '.author-born-date::text')
        loader.add_css('author_bio', '.author-description::text')
        loader.add_css('author_bornlocation', '.author-born-location::text')
        yield loader.load_item()
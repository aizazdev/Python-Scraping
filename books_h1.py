import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksH1Spider(CrawlSpider):
    name = 'books_h1'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       items = response.xpath('//h1/text()').getall()
       for i in items:
           yield {
               'h1': i,
               'url': response.url
           }

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        data = {
            'quote':  response.css('.text::text').getall(),
            'author':  response.css('[itemprop = "author"]::text').getall(),
            'tags': response.css('.tag::text').getall()
        }
        yield data
        next_url = response.css('.next a::attr(href)').get() 
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)
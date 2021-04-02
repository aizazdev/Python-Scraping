import scrapy


class AuthorsPySpider(scrapy.Spider):
    name = 'authors.py'
   # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quotes = response.xpath('//div//div[@class="quote"]/span[@class="text"]/text()').getall()
        links = response.xpath('//div//div[@class="quote"]/span/a/@href').getall()
    
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(url=link, callback=self.parse_authors)
            
    
    def parse_authors(self, response):
        author_data = {
            "author": response.xpath('//div/div[@class="author-details"]/h3/text() ').get(),
            "data": response.xpath('//div/div[@class="author-details"]/p/span[@class="author-born-date"]/text()').get()
        }
        yield author_data
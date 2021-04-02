import scrapy


class ContentSpider(scrapy.Spider):
    name = 'content'
    #allowed_domains = ['en.wikipedia.org/wiki/Data_science#:~:text=Data%20science.%20Data%20science%20is%20an%20interdisciplinary%20field,is%20a%20%22concept%20to%20unify%20statistics%2C%20data%20analysis%2C']
    start_urls = ['http://en.wikipedia.org/wiki/Data_science#:~:text=Data%20science.%20Data%20science%20is%20an%20interdisciplinary%20field,is%20a%20%22concept%20to%20unify%20statistics%2C%20data%20analysis%2C/']

    def parse(self, response):
        self.log(f'My log is {response.url}')
        data = {
            'number': response.css('.tocnumber::text').getall(),
            'text': response.css('.toctext::text').getall(),
        }

        yield data

        
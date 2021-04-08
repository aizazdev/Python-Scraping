import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/gp/most-wished-for/books']

    def parse(self, response):
        containers = response.xpath('//li[@role="gridcell"]')
        for container in containers:     
            heading = container.xpath('.//span/a[@class="a-link-normal"]/div/text()').extract_first().strip()
            author = container.xpath('.//span//div/a/text()').get()
            rating =  container.xpath('.//span//div/a/i/span/text()').get()
            total_reviews = container.xpath('.//span//div/a[2]/text()').get() 
            yield {
                "Heading": heading,
                "Author": author,
                "Ratings": rating,
                "Total Reviews": total_reviews
            }
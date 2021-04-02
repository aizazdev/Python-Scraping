import scrapy


class ImagesSpider(scrapy.Spider):
    name = 'images'
    start_urls = ['https://www.xm.com/']

    def parse(self, response):
        urls = response.css('img::attr(src)').getall()
        clean_urls = []

        for i in urls:
            clean_urls.append( response.urljoin( i ) )
        
        yield {
            'image_urls': clean_urls
        }
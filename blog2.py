import scrapy

class Blog2PySpider(scrapy.Spider):
    name = 'blog2.py'
 #   allowed_domains = ['http://scrapeit.home.blog//']
    start_urls = ['http://scrapeit.home.blog/']

    def parse(self, response):
        posts = response.css('.entry')
        for post in posts:
            data = {
                'header': post.css('.entry-title a::text').get(),
                'paragraph': post.css('.entry-content p::text').get(),
                'author': post.css('.entry-footer a::text').get(),
                'date': post.css('.entry-footer .entry-date::text').get(),
                'tags': post.css('.entry-footer .tags-links a::text').get()
            }
            yield data
        
        next_page = response.css('.next::attr(href)').get()
        if next_page:
            req = scrapy.Request(url = next_page, callback=self.parse)
            yield req
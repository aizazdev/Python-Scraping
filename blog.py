import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = ['http://scrapeit.home.blog//']

    def parse(self, response):
        self.log(f"url is {response.url}")
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

import scrapy


class PlayersPySpider(scrapy.Spider):
    name = 'players.py'
    allowed_domains = ['www.nfl.com']
    start_urls = ['https://www.nfl.com/players/']

    def parse(self, response):
        links = response.css('.d3-o-tabs > li > a::attr(href)').get()
        link = response.urljoin(links)
        yield scrapy.Request(url=link, callback=self.parse_players_list)

        # for link in links:
        #     link = response.urljoin(link)
        #     yield scrapy.Request(url=link, callback=self.parse_players_list)

    def parse_players_list(self, response):
        links = response.css(".nfl-o-cta--link::attr(href)").get()   
        link = response.urljoin(links)
        yield scrapy.Request(url=link, callback=self.parse_players_profile)

        # for link in links:
        #     link = response.urljoin(link)
        #     yield scrapy.Request(url=link, callback=self.parse_players_profile)

    def parse_players_profile(self, response):
        links = response.css('li:nth-child(3) .nfl-o-cta--secondary::attr(href)').get()
        link = response.urljoin(links)
        yield scrapy.Request(url=link, callback=self.parse_players_detail)

    def parse_players_detail(self, response):
        player_name = response.css('.nfl-c-player-header__title::text').get()
        year = response.css('select option[selected]::text').get()
        yield {
            'Player Name': player_name,
            'Year': year
        }
        
        # for t in response.css('table'):
        #     seasons = t.css('.nfl-t-stats__title > h3 ::text').get()   
            
        #     for h in t.css('table > thead > tr'):
        #         headings = h.css("th:text").get()
        #     for b in t.css("table > tbody > tr"):
        #         data = b.css("td::text").get()

        #         yield {
        #             'Player Name': player_name,
        #             'Year': year,
        #             'Season': seasons,
        #             'Heading': headings,
        #             'Data': data
        #         }
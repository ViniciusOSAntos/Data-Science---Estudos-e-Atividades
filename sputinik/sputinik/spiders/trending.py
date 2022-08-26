from urllib import response
import scrapy


class TrendingSpider(scrapy.Spider):
    name = 'trending'
    allowed_domains = ['www.sputnikmusic.com']
    start_urls = ['https://www.sputnikmusic.com/']

    def parse(self, response):
        trending = response.xpath("//table[2]/tbody/tr[2]/td/table/tbody/tr")
        for trend in trending:
            yield{
                'nome_banda': trend.xpath(".//a[@class='tooltip']/font[@color='#333333' and @size='2']/text()").get(),
            }

from urllib import response
import scrapy


class TrendingSpider(scrapy.Spider):
    name = 'trending'
    allowed_domains = ['www.sputnikmusic.com']
    start_urls = ['https://www.sputnikmusic.com/bands/Iron-Maiden/70/']

    def parse(self, response):
        # Pega o nome de todos os albuns da banda
        # albuns = response.xpath("//b/a/font/text()").get()
        # 'nota': response.xpath("//center/font/b/text()").getall()
        albuns = response.xpath("//td[@valign='top']")
        for album in albuns:
            yield{
                'nome': album.xpath(".//b/a/font/text()").get(),
                'nota': album.xpath(".//center/font/b/text()").get(),
                'ano': album.xpath(".//tr/td/font[@size='1']/text()").get()
            }

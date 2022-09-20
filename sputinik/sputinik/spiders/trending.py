from urllib import response
import scrapy


class TrendingSpider(scrapy.Spider):
    name = 'trending'
    allowed_domains = ['www.sputnikmusic.com']
    start_urls = ['https://www.sputnikmusic.com/']

    def parse(self, response):
        cont = 1
        trending = response.xpath("//tr/td[1][contains(@style, 'border-bottom:1px solid #ddd;')][not(contains(@width, '70%'))]")
        for trend in trending:
            yield{
                'posicao': cont,
                'nome_banda': trend.xpath("normalize-space(.//a[@class='tooltip']/font[@color='#333333' and @size='2']/text())").get(),
                'nome_album': trend.xpath(".//a[@class='tooltip']/font[@color='#333333' and @size='2']/span/text()").get()
            }
            cont = cont + 1

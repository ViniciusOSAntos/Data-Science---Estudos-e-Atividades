import scrapy


class AlbumSpider(scrapy.Spider):
    name = 'album'
    allowed_domains = ['www.sputnikmusic.com']
    start_urls = ['https://www.sputnikmusic.com/bands/Iron-Maiden/70/', 'https://www.sputnikmusic.com/bands/Opeth/932/','https://www.sputnikmusic.com/bands/Sleep/1675/']

    def parse(self, response):
        # Pega o nome de todos os albuns da banda
        # albuns = response.xpath("//b/a/font/text()").get()
        # 'nota': response.xpath("//center/font/b/text()").getall()
        albuns = response.xpath("//td[@valign='top'][contains(@style,'padding-right:5px')]")
        for album in albuns:
            yield{
                'nome_banda': response.xpath("//tr/td/font[@size='6']/b/text()").get(),
                'nome_album': album.xpath(".//b/a/font/text()").get(),
                'nota': album.xpath(".//center/font/b/text()").get(),
                'ano': album.xpath("normalize-space(.//td/font[@size='1' and @color='#999999']/text())").get(),
                'votes': album.xpath(".//center/font[2]/text()").get(),
                # 'minha_nota': album.xpath(".//center/font[1]/text()").get() //precisa logar
            }

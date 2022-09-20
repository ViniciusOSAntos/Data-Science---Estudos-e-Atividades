import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from shutil import which


class AlbumSpider(scrapy.Spider):
    name = 'album'
    allowed_domains = ['www.sputnikmusic.com']
    start_urls = ['https://www.sputnikmusic.com/bands/Iron-Maiden/70/',
                  'https://www.sputnikmusic.com/bands/Opeth/932/',
                  'https://www.sputnikmusic.com/bands/Sleep/1675/']

    # Selenium

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.sputnikmusic.com/")

        driver.find_element_by_xpath('//*[@id="tabnav"]/li[1]/a').click()
        driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input').send_keys('TheNameless01')
        driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[1]/form/table/tbody/tr[3]/td[2]/input').send_keys('vasco10')
        driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[1]/form/table/tbody/tr[4]/td/input[7]').click()

        driver.get("https://www.sputnikmusic.com/bands/Iron-Maiden/70/")
        self.html = driver.page_source
        driver.close()
    # Scrapy

    def parse(self, response):
        # get das tags que englobam as informações principais
        resp = Selector(text=self.html)
        albuns = resp.xpath(
            "//td[@valign='top'][contains(@style,'padding-right:5px')]"
            )
        for album in albuns:
            yield{
                'nome_banda': resp.xpath("//tr/td/font[@size='6']/b/text()").get(),
                'nome_album': album.xpath(".//b/a/font/text()").get(),
                'nota': album.xpath(".//center/font/b/text()").get(),
                'ano': album.xpath("normalize-space(.//font[@size='1' and @color='#999999']/text())").get(),
                'votes': album.xpath(".//center/font[2]/text()").get(),
                'minha_nota': album.xpath(".//center/font[1]/text()").get()
            }

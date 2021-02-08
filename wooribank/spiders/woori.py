import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from wooribank.items import Article


class WooriSpider(scrapy.Spider):
    name = 'woori'
    start_urls = ['https://spot.wooribank.com/pot/Dream?withyou=BPPBC0009']

    def parse(self, response):
        rows = response.xpath('//tbody//tr')
        for row in rows:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = row.xpath('.//a/@title').get()
            date = row.xpath('./td[4]//text()').get()
            date = datetime.strptime(date, '%Y.%m.%d')
            date = date.strftime('%Y/%m/%d')

            item.add_value('title', title)
            item.add_value('date', date)

            yield item.load_item()

# response.xpath('').get()


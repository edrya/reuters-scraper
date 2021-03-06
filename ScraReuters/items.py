# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class NewsItem(Item):
    title = Field()
    link = Field()
    sectors = Field()
    text = Field()
    date = Field()
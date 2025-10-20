# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UindknewsItem(scrapy.Item):
    url = scrapy.Field()
    news_title = scrapy.Field()
    author = scrapy.Field()
    issued = scrapy.Field()
    news_content = scrapy.Field()
    

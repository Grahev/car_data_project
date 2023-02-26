# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UsedcarsniItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class UsedcarItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    milage = scrapy.Field()
    transmission = scrapy.Field()
    fuel_type = scrapy.Field()
    body_style = scrapy.Field()
    engine_size = scrapy.Field()
    doors = scrapy.Field()
    color = scrapy.Field()
    location = scrapy.Field()
    timestamp = scrapy.Field()
    link = scrapy.Field()
    phone = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
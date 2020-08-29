# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Yijing64Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    # urls = scrapy.Field()
    # 本卦名
    hexagram1 = scrapy.Field()
    # 互卦
    hexagram2 = scrapy.Field()
    # 错卦
    hexagram3 = scrapy.Field()
    # 综卦
    hexagram4 = scrapy.Field()
    # 周易卦详解
    hexagram = scrapy.Field()
    # 周易1爻详解
    one_yao = scrapy.Field()
    # 周易2爻详解
    two_yao = scrapy.Field()
    # 周易3爻详解
    san_yao = scrapy.Field()
    # 周易4爻详解
    si_yao = scrapy.Field()
    # 周易5爻详解
    wu_yao = scrapy.Field()
    # 周易6爻详解
    liu_yao = scrapy.Field()

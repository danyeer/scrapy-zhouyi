import scrapy
from yijing64.items import Yijing64Item
# import pymysql


class ZhouyiSpider(scrapy.Spider):
    name = 'zhouyi'
    allowed_domains = ['m.zhouyi.cc']
    start_urls = ['https://m.zhouyi.cc/zhouyi/yijing64/']

    def parse(self, response):
        li_list = response.xpath("//div[@class='gualist1 tip_text']/ul/li")

        for li in li_list:
            item = Yijing64Item()
            item['name'] = li.xpath("./a/text()").extract_first()
            # item['urls'] = li.xpath("./a/@href").extract_first()
            detail_urls = 'https://m.zhouyi.cc' + \
                li.xpath("./a/@href").extract_first()

            if detail_urls is not None:
                yield scrapy.Request(detail_urls, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta["item"]
        item['hexagram1'] = response.xpath("//div/table/tbody/tr[3]/td[1]/text()").extract_first().strip()
        item['hexagram2'] = response.xpath("//div/table/tbody/tr[3]/td[2]/text()").extract_first().strip()
        item['hexagram3'] = response.xpath("//div/table/tbody/tr[3]/td[3]/text()").extract_first().strip()
        item['hexagram4'] = response.xpath("//div/table/tbody/tr[3]/td[4]/text()").extract_first().strip()
        # item['hexagram'] = response.xpath("//div[@class='tip_text'][1]").extract_first().strip()
        # item['one_yao'] = response.xpath("//div[@class='tip_text'][2]").extract_first().strip()
        # item['two_yao'] = response.xpath("//div[@class='tip_text'][3]").extract_first().strip()
        # item['san_yao'] = response.xpath("//div[@class='tip_text'][4]").extract_first().strip()
        # item['si_yao'] = response.xpath("//div[@class='tip_text'][5]").extract_first().strip()
        # item['wu_yao'] = response.xpath("//div[@class='tip_text'][6]").extract_first().strip()
        # item['liu_yao'] = response.xpath("//div[@class='tip_text'][7]").extract_first().strip()
        yield item
        # hexagram_list = response.xpath(
        #     "//div/table/tbody/tr[3]/td/text()").extract()
        # for i, v in enumerate(hexagram_list):
        #     # print("=="*10)
        #     # print(i,index)
        #     if i == 0:
        #         item['hexagram1'] = v.strip()
        #     elif i == 1:
        #         item['hexagram2'] = v.strip()
        #     elif i == 2:
        #         item['hexagram3'] = v.strip()
        #     else:
        #         item['hexagram4'] = v.strip()
        #     yield item
            # print(item)

    # def __init__(self):
    # 	con = pymysql.connect(host=settings['MYSQL_HOST'], user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASS'], db=settings['MYSQL_DB'],charset='utf8')
    # 	cur = con.cursor() # 创建数据库连接，定义连接指针
    # 	con.close()

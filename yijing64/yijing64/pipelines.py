# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql
from scrapy.utils.project import get_project_settings


class Yijing64Pipeline(object):

    def __init__(self):
        settings = get_project_settings()
        self.conn = pymysql.connect(host=settings.get('MYSQL_HOST'), user=settings.get('MYSQL_USER'),
                                    passwd=settings.get('MYSQL_PASS'), db=settings.get('MYSQL_DB'), charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()
        # self.f = open("yijing_pipeline.json", "wb")

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + ", \n"
        # self.f.write(content.encode("utf-8"))
        # sql语句
        insert_sql = """
        insert into main_hexagram(id,name,hexagram1,hexagram2,hexagram3,hexagram4) VALUES(%s,%s,%s,%s,%s,%s)
        """
        # 执行插入数据到数据库操作
        self.cursor.execute(
            insert_sql, (item['name'].split("、")[0], item['name'], item['hexagram1'], item['hexagram2'], item['hexagram3'], item['hexagram4']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

        return item

    def close_spider(self, spider):
        # self.f.close()
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

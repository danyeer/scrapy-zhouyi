# 处理爬取到的数据 插入mysql
import json
import pymysql


class InitDB(object):
    """docstring for initDB"""

    def __init__(self):
        self._conn = pymysql.connect(
            host='192.168.1.82', user='root', passwd='ddzb1234', db='hexagram', charset='utf8')

    @property
    def conn(self):
        return self._conn


db = InitDB()
myconn = db.conn
mycursor = myconn.cursor()

quotes = json.load(open('yijing_pipeline.json', encoding='utf-8'))
# print(quotes)
# with open('yijing_pipeline2.json', 'r', encoding='utf-8') as fp:
#     # contents = json.load(fp)
#     # print(json.dumps(contents))
#     papers = []
#     for line in fp.readlines():
#         print(line)
#         papers.append(json.loads(line))

# for node in papers:
#     # print(content)
#     sql = 'select id,name from main_hexagram where name = "%s"' % (
#         node['name'])
#     res = cursor.execute(sql)
#     print(res)


for quote in quotes:
    print(quote['name'])
    # sql = 'select id,name from main_hexagram where name = "%s"' % (
    #     quote['name'])
    # mycursor.execute(sql)
    # data = mycursor.fetchall()
    # print(data)
    insert_sql = """
        insert into main_hexagram_detail(hexagram_id,hexagram,one_yao,two_yao,san_yao,si_yao,wu_yao,liu_yao) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """
    mycursor.execute(insert_sql, (quote['name'].split("、")[0], quote['hexagram'], quote['one_yao'],
                                  quote['two_yao'], quote['san_yao'], quote['si_yao'], quote['wu_yao'], quote['liu_yao']))
    myconn.commit()
mycursor.close()
myconn.close()

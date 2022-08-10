# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class BilibiliPipeline:
	def open_spider(self, spider):
		self.fp = open('./bilibili.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		self.fp.write(str(item))
		return item

	def close_spider(self, spider):
		self.fp.close()


class MySQLPipeline:
	def open_spider(self, spider):
		self.conn = pymysql.connect(
			host="127.0.0.1",
			port=3306,
			user="root",
			password="123456",
			db="bilibili",
			charset="utf8",
		)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		sql = 'insert into videos(title,video,up,up_space,play,date_time) values("{}","{}","{}","{}","{}","{}")'.format(
			item['title'], item['video'], item['up'], item['up_space'], item['play'], item['date']
		)
		try:
			self.cursor.execute(sql)
		except:
			print("插入失败：")
			print(item)
		finally:
			return item

	def close_spider(self, spider):
		self.cursor.close()
		self.conn.close()

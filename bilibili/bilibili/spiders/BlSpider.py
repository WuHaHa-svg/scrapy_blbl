import scrapy
from ..items import BilibiliItem


class BlspiderSpider(scrapy.Spider):
	name = 'BlSpider'
	allowed_domains = ['search.bilibili.com']
	start_urls = ['https://search.bilibili.com/']
	keyword = ''
	base_url = 'https://search.bilibili.com/all'

	def parse(self, response):
		self.keyword = input("输入关键字：")
		for i in range(1, 51):
			url = self.base_url + '?keyword=' + self.keyword + "&page=" + str(i)
			yield scrapy.Request(url=url, callback=self.parse_do)

	def parse_do(self, response):
		# print("successfully!")
		li_list = response.xpath('//ul[@class="video-list clearfix"]/li')
		# if not li_list:
		# 	return
		# print(div_list)
		for item in li_list:
			title = item.xpath('.//a[@class="title"]/@title').extract_first()
			video = "https:" + item.xpath('.//a[@class="title"]/@href').extract_first()
			up = item.xpath('.//a[@class="up-name"]/text()').extract_first()
			up_space = "https:" + item.xpath('.//a[@class="up-name"]/@href').extract_first()
			date = item.xpath('.//span[@class="so-icon time"]/text()').extract_first().strip()
			play = item.xpath('.//span[@class="so-icon watch-num"]/text()').extract_first().strip()
			video_body = BilibiliItem(title=title, video=video, up=up, up_space=up_space, play=play, date=date)
			yield video_body

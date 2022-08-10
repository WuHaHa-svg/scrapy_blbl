# _*_ coding:utf-8 _*_
# 开发时间：2022/8/8 20:29
# 开发者：吴哈哈
# 项目名称：代理
import requests
from lxml import etree

url = 'https://free.kuaidaili.com/free/inha/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

text = requests.get(url=url, headers=headers).text
tree = etree.HTML(text)
tr_list = tree.xpath('//*[@id="list"]/table/tbody/tr')
# print(tr_list)
for item in tr_list:
	ip = item.xpath('./td[1]/text()')[0]
	port = item.xpath('./td[2]/text()')[0]
	pro = item.xpath('./td[4]/text()')[0]
	if pro == "HTTP":
		proxy = "\'" + "http://" + ip + ":" + port + "\'" + ','
		print(proxy)
	if pro == "HTTPS":
		proxy = "\'" "https://" + ip + port + "\'" + ","
		print(proxy)



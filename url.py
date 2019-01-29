#encoding: utf-8
import requests	#爬虫
import re	#正则
import codecs	#字符串编码
import time
#爬虫访问模拟浏览器的请求头信息（http header)
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#目标网站地址
url = 'https://sukebei.nyaa.si/?f=0&c=0_0&q=&s=seeders&o=desc'
result = requests.get(url,headers=headers)	#以GET方法获取网页信息
result.encoding = 'utf-8'	#网站编码
#自定义函数
def GetTorrent():
	tor = r'(/download/.*?)\"'
	com = r'\d\d" title="(.*?)\"'
	torrent = re.findall(tor,result.text)
	comment = re.findall(com,result.text)
	aa=0
	for i in range(0,75):
		print('Just do it!')
		f = open('magnet.txt','a',encoding='utf-8')
		a = comment[i]
		b = torrent[i]
		f.write(str(a))
		f.write('\n')
		f.write(str(b))
		f.write('\n')
		f.close()
		dltor = open(str(comment[i])+'.torrent','wb')
		c = 'https://sukebei.nyaa.si'+torrent[i]
		temp=requests.get(c)
		dltor.write(temp.content)
		dltor.close()
		print(c)
GetTorrent()

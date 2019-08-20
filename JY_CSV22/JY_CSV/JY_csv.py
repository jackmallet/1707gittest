# -*- coding: utf-8 -*-\
import xlrd,re,xlwt,csv,requests
from xlutils.copy import copy
import time
import eventlet

class JY_csv(object):
	def __init__(self):
		# 打开excel表格
		self.data = xlrd.open_workbook(r'总数据源2019.8.08.xls')
		# 复制excel表并不改变属性
		self.newWb = copy(self.data)
		#取sheet为总列表的表
		self.newWs = self.newWb.get_sheet(1)
		self.headers = {
			'User-Agent' : 'Mozilla/5.0'
		}
		self.i = 1493
	
	def read_excel(self):
		# 获取excel中sheet为总列表
		sheet_name = self.data.sheet_names()[1]
		sheet = self.data.sheet_by_name(sheet_name)
		# excel表sheet的名称，行数，列数
		# print(sheet.name, sheet.nrows, sheet.ncols)
		# 获取所有url
		cols = sheet.col_values(2)
		# print(cols)
		# 以列表形式返回所有excel中的url
		return cols[1:]

	def write_excel(self, urls):
		eventlet.monkey_patch()
		# 遍历去重后的url集合
		for url in urls:
			print(url)
			self.newWs.write(self.i, 2, url)
			try:
				with eventlet.Timeout(20, False):
					res = requests.get('http://' + url, headers=self.headers)
					res.encoding = 'utf-8'
					title = re.search(r'<title>(.*?)</title>', res.text, re.S).group(1).strip()
					self.newWs.write(self.i, 3, title)
					self.newWb.save('总数据源2019.8.09.xlsx')
					print(title)
			except Exception as e:
				pass
			self.i += 1

	def csv_read(self):
		# 打开csv(以读的形式)
		with open('千里马广东8月111.csv', 'r') as f:
			# 获取csv中的内容
			url_infos = csv.reader(f)
			list = []
			for url in url_infos:
				j = re.sub(r'http.*?//', '', url[0]).strip()
				j = re.sub(r'[%|?|:|）|（|。|、|→|【|】|“|”|,|，|(|@]\w*', '', j).strip()
				list.append(j)
		# print(list[1:])
		return list[1:]

	def txt_write(self, urls):
		with open('gd.txt', 'w', encoding='utf-8') as f:
			for url in urls:
				f.writelines(url + '\n') 

	def main(self, url_excel, url_csv):
		set1 = set()
		set2 = set()
		set3 = set()
		# 对excel表的数据进行分割
		for x in url_excel:
			url = re.sub(r'http.*?://', '', x)
			url = re.sub(r'/', '', url)
			url = re.sub(r':\w*', '', url)
			set1.add(url)
			set2.add(url)
		print(set1)
		print(len(set1))
		# 对csv的表进行分割
		for y in url_csv:
			url = re.sub(r'http.*?://', '', y)
			set1.add(url)
		print(len(set1))
		# 用set集合进行去重
		for z in set2:
			set1.remove(z)
		print(len(set1))
		# 将http加进去
		for urls_set1 in set1:
			for urls_csv in url_csv:
				if urls_set1 in urls_csv:
					set3.add(urls_csv)
		return set3

	def run(self):
		# 获取excel中所有的url
		url_excel = self.read_excel()
		# 获取csv中的所有url
		url_csv = self.csv_read()
		# print(url_csv)
		# 对所有的url进行去重
		urls = self.main(url_excel, url_csv)
		print(urls)
		self.txt_write(urls)
		# 填写进excel表并进行标题爬取
		# self.write_excel(urls)

if __name__ == '__main__':
	JY_csv().run()
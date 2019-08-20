# -*- coding:utf-8 -*-
# Author :PS
# @Time :2019/4/12 12:27

# with open('安全漏洞.csv','a') as csvfile:
#    	w=csv.DictWriter(csvfile,items.keys())
#    	w.writerow(items)
# import csv
#
# with open('A_list.csv', 'a') as csvfile:
#     fieldnames = ['name', 'url']
#     w = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     A_set = set()
#     with open('火标网.csv','r',encoding='gbk') as f:
#         f_lis=f.readlines()
#         for word in f_lis[1:]:
#             word_lis=word.split(',')
#             try:
#                 items={"name":word_lis[3],"url":word_lis[2]}
#                 if word_lis[2] not in A_set:
#                     w.writerow(items)
#                     A_set.add(word_lis[2])
#             except:
#                 pass
#     with open('火车头爬虫.csv','r',encoding='gbk') as f:
#         f_lis=f.readlines()
#         for word in f_lis:
#             word_lis=word.split(',')
#             try:
#                 items={"name":word_lis[5],"url":word_lis[0]}
#                 if word_lis[0] not in A_set:
#                     w.writerow(items)
#                     A_set.add(word_lis[0])
#             except:
#                 pass
#     with open('火车头2.csv','r',encoding='gbk') as f:
#         f_lis=f.readlines()
#         for word in f_lis:
#             word_lis=word.split(',')
#             try:
#                 items={"name":word_lis[1],"url":word_lis[0]}
#                 if word_lis[0] not in A_set:
#                     w.writerow(items)
#                     A_set.add(word_lis[0])
#             except:
#                 pass
# print(len(A_set))

import re,redis


class QingXi(object):
    def __init__(self):
        self.Li = set()
        self.Lis = []
        self.surffix = []
        self.pool = redis.ConnectionPool(host='120.77.159.174', port=6379, db=14)
        self.r = redis.Redis(connection_pool=self.pool)

    def QX(self, List):
        for x in List:
            L = re.sub(r'http://|https://|\.com|\.cn', '', x, re.S)
            self.Li.add(L)

        for i in self.Li:
            z = 0
            for j in List:
                if i in j:
                    z += 1
                    if z == 1:
                        self.Lis.append(j)
        return self.Lis

    def get_data(self):
        r_data = self.r.smembers('source_link')
        for x in r_data:
            print(x.decode())
            self.surffix.append(x.decode())
        List = self.QX(self.surffix)
        return List

class Insert_data(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='120.77.159.174', port=6379, db=12)
        self.r = redis.Redis(connection_pool=self.pool)

    def inset_data(self):
        r_data = QingXi().get_data()
        print(r_data)
        for x in r_data:
            print('11')
            self.r.sadd('guangdong_link', x)

if __name__ == "__main__":
    Insert_data().inset_data()
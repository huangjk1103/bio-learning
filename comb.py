#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import sys

def main():
	
	f = open(sys.argv[2],'r')
	inlin = f.readlines()
	sortlist = []
	for line in inlin:
		temp1 = line.strip('\n')
		sortlist.append(temp1)      #设置排序列表  sortlist
	print ('------------this is the sortlist------------')
	print (sortlist)
	print ('--------------------end---------------------')
	df = pd.read_csv(sys.argv[1],header = 0)
	pdf = pd.DataFrame(df)    #将数据转成dataframe
	pdf['work'] = pdf['work'].astype('category').cat.set_categories(sortlist)
	pdf_sortes = pdf.sort_values(by = ['work'],ascending = False)
	pdf_sortes.to_csv('/tsttt.csv')   # 临时	
	
	data = pd.read_csv('/tsttt.csv',header = 0)   #临时文件
	pdata = pd.DataFrame(data)
	pdata['work'].to_csv('/0.csv',header = True)    #临时文件    work是列名
	
	k = 1
	for i in sortlist:
		pdata[i].to_csv('/%s.csv' %k,header = True)    #临时文件
		k = k + 1
	wo = pd.read_csv('/0.csv', header = 0)    #临时文件
	pwo = pd.DataFrame(wo)
	m = 0
	n =1
	while m < 117:
    		pd.merge(pd.DataFrame(pd.read_csv('/%s.csv' %m)),pd.DataFrame(pd.read_csv('/%s.csv' %n)),how = 'outer').to_csv('/%s.csv' %n)
    		m = m +1
    		n = n +1

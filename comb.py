#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
f = open('/Users/mac/Desktop/name.txt','r')
inlin = f.readlines()
sortlist = []
for line in inlin:
	temp1 = line.strip('\n')
	sortlist.append(temp1)      #设置排序列表  sortlist
print ('------------this is the sortlist------------')
print (sortlist)
print ('--------------------end---------------------')
df = pd.read_csv('/Users/mac/Desktop/tst.csv',header = 0)
pdf = pd.DataFrame(df)    #将数据转成dataframe
pdf['work'] = pdf['work'].astype('category').cat.set_categories(sortlist)
pdf_sortes = pdf.sort_values(by = ['work'],ascending = False)
pdf_sortes.to_csv('/Users/mac/Desktop/tsttt.csv')
data = pd.read_csv('/Users/mac/Desktop/tsttt.csv',header = 0)
pdata = pd.DataFrame(data)


pdata['work'].to_csv('/Users/mac/Desktop/comb/0.csv',header = True)
k = 1
for i in sortlist:
	pdata[i].to_csv('/Users/mac/Desktop/comb/%s.csv' %k,header = True)
	k = k + 1

wo = pd.read_csv('/Users/mac/Desktop/comb/0.csv', header = 0)
pwo = pd.DataFrame(wo)
m = 0
n =1
while m < 117:
    pd.merge(pd.DataFrame(pd.read_csv('/Users/mac/Desktop/comb/%s.csv' %m)),pd.DataFrame(pd.read_csv('/Users/mac/Desktop/comb/%s.csv' %n)),how = 'outer').to_csv('/Users/mac/Desktop/comb/%s.csv' %n)
    m = m +1
    n = n +1
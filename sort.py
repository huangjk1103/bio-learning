#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
f = open('/Users/mac/Desktop/CAZyme_analysis/CAZyme_analysis_E7_2.txt','r')
inlin = f.readlines()
sortlist = []
for line in inlin:
	temp1 = line.strip('\n')
	sortlist.append(temp1)      #设置排序列表  sortlist
print ('------------this is the sortlist------------')
print (sortlist)
print ('--------------------end---------------------')
df = pd.read_csv('/Users/mac/Desktop/CAZyme_analysis/E7_related_geneseq.csv',header = 0)
pdf = pd.DataFrame(df)    #将数据转成dataframe
pdf['name'] = pdf['name'].astype('category').cat.set_categories(sortlist)
pdf_sortes = pdf.sort_values(by = ['name'],ascending = False)
pdf_sortes.to_csv('/Users/mac/Desktop/CAZyme_analysis/E7_related_geneseq_2.csv')
#!/usr/bin/python
#encoding = utf-8
import pandas as pd

with open('/Users/mac/Desktop/浮霉状菌/E7_8797_G_annotation_promer-总体.csv') as file1:
    csv_file = csv.DictReader(file1,delimiter = ',')
    for i in csv_file:
        l1 = []
        l1.append(i['id'])
        print (l1)
        

with open('/Users/mac/Desktop/浮霉状菌/transcriptome/diffanalysis6db649/combineeeafd4/result.csv') as file2:
    csv_file2 = csv.DictReader(file2,delimiter = ',')
    for j in csv_file2:
        l2 = []
        l2.append(j['id'])


    

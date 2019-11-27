#!/usr/bin/python
#encoding = utf-8
import pandas as pd
import sys

def Usage():
    print('usage:python *.py [csv_file1] [csv_file2])
          
def main():
          
    with open(sys.argv[1]) as file1:
        csv_file = csv.DictReader(file1,delimiter = ',')
        for i in csv_file:
            l1 = []
            l1.append(i['id'])
            print (l1)
        

    with open(sys.argv[2]) as file2:
        csv_file2 = csv.DictReader(file2,delimiter = ',')
        for j in csv_file2:
            l2 = []
            l2.append(j['id'])
try:
          main()
except:
          Usage()

    

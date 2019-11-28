#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from lxml import html
import time
from bs4 import BeautifulSoup
import os
import re

def readid():
    with open('/Users/mac/Desktop/Planctomycetes/genomeid.txt','r') as idtxt:     #我的电脑会给txt文件的后面加上/r/n
        #file = open('/Users/mac/Desktop/Planctomycetes/ftp.txt','r')
        for x in idtxt:
            print (x)
            url = ("https://www.ncbi.nlm.nih.gov/genomes/Genome2BE/genome2srv.cgi?action=GetGenomes4Grid&genome_id={}&genome_assembly_id=&king=Bacteria&mode=2&flags=1&page=1&pageSize=100".format(x.strip('\r\n')))
            r = requests.get(url).content# 获取首页的html
            sel = html.fromstring(r)
            data =sel.xpath('//a/@href')
            for i in data:
                print (i)
                #file.write(s)
           # time.sleep(5)
       # file.close()


#def match():
   #with open ('/Users/mac/Desktop/Planctomycetes/ftp.txt','r') as ftp:
   #     for i in ftp:
   ##         if re.match('581',i) != None:
    #            print(i.strip('\r\n') + i.strip('\r\n').split('1')[-1])

        
readid()
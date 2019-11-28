#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from lxml import html
import time
from bs4 import BeautifulSoup
import os
import re

with open ('/Users/mac/Desktop/Planctomycetes/ftp.txt','r') as ftp:
        for i in ftp:
            if re.match('ftp',i) != None:
                t = i.strip('\r\n')+'/'+i.split('/')[-1].strip('\r\n')+'_protein.faa.gz'
                print (t.strip('\r')+'---o--/Users/mac/Desktop/Planctomycetes/'+i.split('/')[-1].strip('\r\n')+'_protein.faa.gz')
                #os.popen('curl i.strip('\r\n') + '/' +i.strip('\r\n').split('1')[-1] + '_protein.faa.gz' -o /Users/mac/Desktop/Planctomycetes/')
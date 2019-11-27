#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pandas as pd


def main():
    dict = {}
    with open('/Users/mac/Desktop/E7_AA.fasta', 'r') as fastaf:
        for line in fastaf:
            if line.startswith('>'):
                name = line.strip().split()[0][1:]
                dict[name] = ''
            else:
                dict[name] += line.replace('\n','')

    with open('/Users/mac/Desktop/CAZyme_analysis/CAZyme_analysis_E7_2.txt','r') as listf:
        for row in listf:
            row = row.strip()
            for key in dict.keys():
                if key == row:
                    temp1 ='>' + key
                    temp2 = dict[key] + '/n'
                    print (temp1+','+temp2)  # cmd 里直接输出csv格式
        #pd.DataFrame([temp4],[temp3]).to_csv('/Users/mac/Desktop/CAZyme_analysis/E7_related_geneseq.csv')  #输出的序列，需要转置
                    
main()

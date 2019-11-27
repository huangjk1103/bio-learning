#!/usr/bin/python
import pandas as pd
obj = pd.read_csv('/Users/mac/Desktop/CD_search_DSM8797_protein_group/CD_search_8797_cog.csv')
temp = pd.read_csv('/Users/mac/Desktop/CD_search_DSM8797_protein_group/COG_pair_list.csv')
data_dict = temp.groupby('Code').Pattern.apply(list).to_dict()
#print [(x, data_dict.get(x, 'null')) for x in obj['Code']]
for x in obj['Code']:
	df = (x,data_dict.get(x, 'null'))
	print (df)


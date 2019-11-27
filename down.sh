#!/bin/bash

cat /Users/mac/Desktop/prokaryotes_refer_genome/prokaryotes.txt | while read line
do
	curl $line
done

#for i in cat ./prokaryotes.txt
	



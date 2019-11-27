#! /usr/bin/python2.7
from Bio import SeqIO
for seq_record in SeqIO.parse("./Desktop/E7-DSM8797_NagB_gene.fasta","fasta"):
    print (seq_record.id)


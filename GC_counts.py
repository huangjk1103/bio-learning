#!/usr/bin/python

from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio import SeqIO
import sys


def usage():
    print('Usage: python GC_counts.py [fasta_file]')

def main():
    for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
        print (seq_record.id)
        print (len(seq_record.seq))
        print (GC(seq_record.seq))


try:
    main()
except IndexError:
    usage()
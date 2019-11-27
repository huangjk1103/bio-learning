#!/usr/bin/python3
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


for AAseq in SeqIO.parse("./E7_protein_group/500.fasta","fasta"):
	if 200<len(AAseq.seq) <=500:
		print (">"+AAseq.id)
		print (AAseq.seq)
	

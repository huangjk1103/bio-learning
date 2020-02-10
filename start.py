
'''
from Bio.Seq import Seq
my_seq = Seq("AGTAACAGTAGCTA")
print (my_seq)
print (my_seq.alphabet)
print (my_seq.complement())
print (my_seq.reverse_complement())
'''

from Bio import SeqIO
for seq_record in SeqIO.parse("./sequence.fasta","fasta"):
    print (seq_record.id)
    print (repr(seq_record.seq))
    print (len(seq_record))
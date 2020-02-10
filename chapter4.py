from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Alphabet import generic_protein
simple_seq = Seq("ATGC")
simple_seq_r = SeqRecord(simple_seq)
print (simple_seq_r.id)
simple_seq_r.id = "AC3432"
print (simple_seq_r.id)
simple_seq_r.description = "what i want to do"
print (simple_seq_r.description)
print (simple_seq_r.seq)

record = SeqIO.read("./sequence.fasta","fasta")
print (record)
print (record.id)
print (record.description)
record.description = "Escherichia coli str. K-12 NagB"
print (record)
print (len(record))
print (record.features)   #未定义，因此位空集


'''
record1 = SeqRecord(Seq("atcg"),id = "test")
record2 = SeqRecord(Seq("atcg"),id = "test")
if record1.seq == record2.seq:
    print ('yes')   #seqrecord比较，可以不要转换string，但需要声明seq，或者id或者其他的feature

protein1 = SeqRecord(Seq("MVODHFJDSJOIFEOFHSJFLKSJLJFLDSHFJHLKFJDSLFHDSFKDJFLKDJF", generic_protein),id = "tset",description = "hhahahaha")
print (protein1.format("fasta"))    #以fasta格式来输出序列方式
'''


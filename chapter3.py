from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio.Alphabet import generic_dna

my_seq = Seq("CGATGCATGCTAGTC",IUPAC.ambiguous_dna)   #后面的IUPAC是对前面的序列进行格式定义，可以是dna或者protein
print (my_seq)
print (my_seq.alphabet)
for index,letter in enumerate(my_seq):
    print("%i %s" %(index,letter))   #替代方式
print (len(my_seq))   #sequence length
print (my_seq[2])    #speific position nucleaicd
print (my_seq.count("TG"))     #motif counts
print (GC(my_seq))   #GC count
print (my_seq[2:7])   #slicing a sequence
print (my_seq[0::3])   #从第0位开始，直到最后，每间隔2个字符，取第三个字符来显示
print (my_seq[::-1])   #反向读数
print (my_seq.reverse_complement().complement())   #同上
print (str(my_seq))
print (my_seq)   #same as above


fasta_format_string = ">Name\n%s\n" %my_seq
print (fasta_format_string)     #将序列转换位string来进行编辑，同时按照fasta格式排列

print (my_seq.lower())   #小写
print (my_seq.lower().upper())    #大写 
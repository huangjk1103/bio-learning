from Bio import SeqIO
for seq1_record in SeqIO.parse("./sequence.fasta", "fasta"):
    print (seq1_record.id)
    print (repr(seq1_record.seq))
    print (len(seq1_record))

with open ("./E7_AA.fasta") as handle:
    print (sum(len(r) for r in SeqIO.parse(handle,"fasta")))

seq_dict = SeqIO.to_dict(SeqIO.parse("./E7_AA.fasta","fasta"))   #将文件按照fasta的格式进行读取，因此，常规的fasta各种feature都将会显示出来，如果没有定义，则系统自动定义
#print (list(seq_dict.keys()))    #字典的keys
#print (list(seq_dict.values()))    #字典的数值
s001 = seq_dict["E7_regene_00001"]
print (s001.description)
print (s001.seq)    #可以直接输出序列内容
print (repr(s001.seq))    #则按照biopython的标准格式来输出序列信息


'''
all_num= []
for seq_record in SeqIO.parse("./E7_AA.fasta","fasta"):
    all_num.append(seq_record.id)
print (all_num)      #提取所有序列的名字
all_num2 = [seq_record.id for seq_record in SeqIO.parse("./E7_AA.fasta","fasta")]
print (all_num2)    #same as above

identifiers = [seq_record.id for seq_record in SeqIO.parse("./E7_AA.fasta","fasta")]
print (identifiers)

record_iterator = SeqIO.parse("./E7_AA.fasta","fasta")
first_record = next(record_iterator)
print (first_record)
second_record = next(record_iterator)
print (second_record.id)

records = list(SeqIO.parse("./E7_AA.fasta","fasta"))
print ("found %i records" % len(records))

'''
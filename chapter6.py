'''
from Bio import AlignIO
alignment = AlignIO.read("aligned file path","stockholm")    #alignIO可以读取已经比对后的文件
print (alignment)

print ("alignment length %i" %alignment.get_alignment_length())   #可以输出能够比对上的区段长度

for record in alignment:
    print ("%s - %s" % (record.seq,record.id))   #分别输出对齐的序列和对应的名字

for record in alignment:
    if record.dbxrefs:       #如果record中有dbxrefs（feature），则继续下面的语句，否则停止
        print ("%s %s" % (record.id, record.dbxrefs)

for record in alignment:
    print (record)    #分别输出参与比对的序列信息，按照fasta文件的格式。
'''
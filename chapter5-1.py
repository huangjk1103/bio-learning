from Bio import SeqIO

orchid_dict = SeqIO.index("./E7_AA.fasta","fasta")
print (list(orchid_dict.keys()))    #单独print (orchid_dict.keys())不能正常显示，报错<dict_keyiterator object at 0x10fe9bbd8>。更改为list后可以显示
seq_record = orchid_dict["E7_regene_10357"]
print (seq_record.description)
print (seq_record.seq)   #这样，可以直接输出序列内容，与to_dict相同
orchid_dict.close


#get_accession方式与to_dict相同

from Bio import SeqIO
def get_accession(record):
    ''' given a SeqRecord, return the accession number as a string.
    e.g. "gi|4324234|emb|Z74324.1|PTZ434324"   ->  "Z74324.1"
    '''
    parts = record.split("_")   #分割符号,这个部分与to_dict不同
    assert len(parts) == 3 and parts[0] == "E7" and parts[1] =="regene"   #assert是判断语句，如果位true，则输出结果，否则无任何显示
    return parts[2]    #返回目标部分

seq_dict = SeqIO.to_dict(SeqIO.index("./E7_AA.fasta","fasta"),key_function=get_accession)
print (seq_dict.keys())



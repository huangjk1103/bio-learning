from Bio import SeqIO
def get_accession(record):
    ''' given a SeqRecord, return the accession number as a string.
    e.g. "gi|4324234|emb|Z74324.1|PTZ434324"   ->  "Z74324.1"
    '''
    parts = record.id.split("_")   #分割符号
    assert len(parts) == 3 and parts[0] == "E7" and parts[1] =="regene"   #assert是判断语句，如果位true，则输出结果，否则无任何显示
    return parts[2]    #返回目标部分

seq_dict = SeqIO.to_dict(SeqIO.parse("./E7_AA.fasta","fasta"),key_function=get_accession)
print (seq_dict.keys())



from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable
coding_dna = Seq("atgcgatgctggtacgctagctag", IUPAC.ambiguous_dna)
print (coding_dna.upper())
templete_dna = coding_dna.reverse_complement()
print (templete_dna.upper())
messager_rna = coding_dna.upper().transcribe()
print (messager_rna)
print (messager_rna.back_transcribe())
print (coding_dna.upper())


print (messager_rna.translate())
print (coding_dna.translate(to_stop=True))   #遇到终止密码子就输出，因此可以不带*

print (coding_dna.translate(table="Vertebrate Mitochondrial"))    #密码子表多种多样，可以参考NCBI
print (coding_dna.translate(table="Bacterial",to_stop= True))   #密码子表多种多样
print (coding_dna.translate(table="Bacterial",cds = True))

standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
bacterial_table = CodonTable.unambiguous_dna_by_name["Bacterial"]
print (standard_table)
print (bacterial_table)
print (bacterial_table.stop_codons)
print (bacterial_table.start_codons)


seq1 = Seq("ATCG",IUPAC.unambiguous_dna)
seq2 = Seq("ATCG",IUPAC.unambiguous_dna)
if str(seq1) == str(seq2):
    print ('yes')   #序列如果需要比较的时候，只能将序列先转换位string，才可以比较
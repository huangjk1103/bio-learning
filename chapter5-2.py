from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from Bio import SeqIO
rec1 = SeqRecord(Seq("MNPIARQLDINPEFVHAGVLPEEKLQIIQQSTPEGLTVMVGDGVNDSAALAAASVGIAVHGGAEASLQVADVYLIVPA", generic_protein),id = "rec1", description = "rec1")
rec2 = SeqRecord(Seq("MNPIARQLDINPEFVHAGVLPEEKLQIIQQSTPEGLTVMVGDGVNDSAALAAASVGIAVHGGAEASLQVADVYLIVPA", generic_protein),id = "rec2", description = "rec1")
rec3 = SeqRecord(Seq("MNPIARQLDINPEFVHAGVLPEEKLQIIQQSTPEGLTVMVGDGVNDSAALAAASVGIAVHGGAEASLQVADVYLIVPA", generic_protein),id = "rec3", description = "rec1")
my_records =  [rec1,rec2,rec3]
SeqIO.write(my_records,"./myexample.faa","fasta")    #按照fasta的文件格式来写入文件
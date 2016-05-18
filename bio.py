from Bio import SeqIO
for seq_record in SeqIO.parse("homo_sapiens.fna", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

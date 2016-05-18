from Bio import SeqIO
for seq_record in SeqIO.parse("homo_sapiens.fna", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

entries = [("Chr 1", "NC_000001.11"),
("Chr 2", "NC_000002.12"),
("Chr 3", "NC_000003.12"),
("Chr 4", "NC_000004.12"),
("Chr 5", "NC_000005.10"),
("Chr 6", "NC_000006.12"),
("Chr 7", "NC_000007.14"),
("Chr 8", "NC_000008.11"),
("Chr 9", "NC_000009.12"),
("Chr 10", "NC_000010.11"),
("Chr 11", "NC_000011.10"),
("Chr 12", "NC_000012.12"),
("Chr 13", "NC_000013.11"),
("Chr 14", "NC_000014.9"),
("Chr 15", "NC_000015.10"),
("Chr 16", "NC_000016.10"),
("Chr 17", "NC_000017.11"),
("Chr 18", "NC_000018.10"),
("Chr 19", "NC_000019.10"),
("Chr 20", "NC_000020.11"),
("Chr 21", "NC_000021.9"),
("Chr 22", "NC_000022.11"),
("Chr X", "NC_000023.11"),
("Chr Y", "NC_000024.10")]

for (name, filename) in entries:
    record = SeqIO.read("homo_sapiens.fna","fasta")
print(name, len(record))

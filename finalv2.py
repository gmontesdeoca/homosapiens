from reportlab.lib.units import cm
from Bio.Graphics import BasicChromosome

entries = [("1", 248956422),
("2", 242193529),
("3", 198295559),
("4", 190214555),
("5", 181538259),
("6", 170805979),
("7", 159345973),
("8", 145138636),
("9", 138394717),
("10", 133797422),
("11", 135086622),
("12", 133275309),
("13", 114364328),
("14", 107043718),
("15", 101991189),
("16", 90338345),
("17", 83257441),
("18", 80373285),
("19", 58617616),
("20", 64444167),
("21", 46709983),
("22", 50818468),
("X", 156040895),
("Y", 57227415)]


max_len = 248956422 #Could compute this
telomere_length = 100000000 #For illustration

chr_diagram = BasicChromosome.Organism()
chr_diagram.page_size = (29.7*cm, 21*cm) #A4 landscape

for name, length in entries:
    cur_chromosome = BasicChromosome.Chromosome(name)
    #Set the scale to the MAXIMUM length plus the two telomeres in bp,
    #want the same scale used on all five chromosomes so they can be
    #compared to each other
    cur_chromosome.scale_num = max_len + 3 * telomere_length

    #Add an opening telomere
    start = BasicChromosome.TelomereSegment()
    start.scale = telomere_length
    cur_chromosome.add(start)

    #Add a body - using bp as the scale length here.
    body = BasicChromosome.ChromosomeSegment()
    body.scale = length
    cur_chromosome.add(body)

    #Add a closing telomere
    end = BasicChromosome.TelomereSegment(inverted=True)
    end.scale = telomere_length
    cur_chromosome.add(end)

    #This chromosome is done
    chr_diagram.add(cur_chromosome)

chr_diagram.draw("simple_chrom.pdf", "Homo sapiens")

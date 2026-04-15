def to_rna(dna_strand):
    dna_strand_buffer = list(dna_strand)
    base_dna = ["G", "C", "T", "A"]
    base_rna = ["C", "G", "A", "U"]
    rna_strand = []
    for letter in dna_strand_buffer:
        if letter == base_dna[0]:
            rna_strand.append(base_rna[0])
        if letter == base_dna[1]:
            rna_strand.append(base_rna[1])
        if letter == base_dna[2]:
            rna_strand.append(base_rna[2])
        if letter == base_dna[3]:
            rna_strand.append(base_rna[3])
    return "".join(rna_strand) or dna_strand
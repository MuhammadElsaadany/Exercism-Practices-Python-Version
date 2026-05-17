def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    differences = [i for index, i in enumerate(strand_a) if i != strand_b[index]]
    return len(differences)
def dna_to_rna(x):
    with open(x) as dna:
        dna = dna.read().strip()
        rna = dna.replace('T', 'U')
        return rna

path = r'rosalind_rna.txt'
print(dna_to_rna(path))

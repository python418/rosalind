def countnt(x):
    with open(x) as dna:
        dna = dna.read()
        A = dna.count('A')
        C = dna.count('C')
        G = dna.count('G')
        T = dna.count('T')
        return f'{A} {C} {G} {T}'
    
path = r"rosalind_dna.txt"
print(countnt(path))

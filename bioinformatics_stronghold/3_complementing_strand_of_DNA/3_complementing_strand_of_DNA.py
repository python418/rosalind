def complemented(x):
    with open(x) as dna:
        dna = dna.read().strip()
        c_1 = dna.replace('A', 'X')
        c_2 = c_1.replace('T', 'A')
        c_3 = c_2.replace('X', 'T')

        c_4 = c_3.replace('C', 'X')
        c_5 = c_4.replace('G', 'C')
        c_6 = c_5.replace('X', 'G')

        return c_6[::-1]
path = r'rosalind_revc.txt'
print(complemented(path))

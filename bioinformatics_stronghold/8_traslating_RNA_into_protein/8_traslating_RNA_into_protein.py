def RNA_into_protein(a, b):
    with open(a) as ct:
        ct = ct.read()
        ct_splitted = ct.split()
        d = {}
    
        nucleotides = [i for i in ct_splitted if len(i) == 3]
        amino_acids = [i for i in ct_splitted if len(i) == 1 or len(i) == 4]
        for i in range(len(amino_acids)):
            d[nucleotides[i]] = amino_acids[i]
    

    with open(b) as rna:
        rna = rna.read().strip()
        nt = [x for x in rna]
        triplet = []

        i = 0
        for x in range(int(len(nt)/3)):
            triplet.append(nt[i]+nt[i+1]+nt[i+2])
            i = i+3
            
        amino = []
        for x in triplet:
            for key, value in d.items():
                if key == x:
                    amino.append(value)

        if 'Stop' in amino:
            del amino[amino.index('Stop'):]
                
        polypeptide = ''
        for amino_acid in amino:
            polypeptide = polypeptide + amino_acid
        return polypeptide


codon_table_path = r'codon_table.txt'
RNA_path = r'rosalind_prot.txt'
write_protein_path = r'protein.txt'
with open(write_protein_path, 'w', encoding = 'utf-8') as file:
    file.write(RNA_into_protein(codon_table_path, RNA_path))

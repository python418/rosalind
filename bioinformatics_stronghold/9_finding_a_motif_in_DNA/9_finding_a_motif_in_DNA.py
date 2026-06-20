def motif(x):
    with open(x) as infile:
        infile = infile.read().strip()
        splitted = infile.splitlines()
        dna = splitted[0]
        search = splitted[1]
        numbers = []
        try:
            for i in range(len(dna) - len(search) + 1):
                if i == dna.index(search, i):
                    numbers.append(i+1)
        except ValueError:
             pass
        return ' '.join(str(num) for num in numbers)
        
read_path = r'rosalind_subs.txt'
write_path = r'solution_path_9.txt'
with open(write_path, 'w', encoding='utf-8') as outfile:
    outfile.write(motif(read_path))
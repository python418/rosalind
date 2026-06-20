def consensus_profile(file_):
    with open(file_) as infile:
        chunks = infile.read().strip().split('>')
    
    dna = []
    for chunk in chunks:
        if chunk.strip():
            lines = chunk.strip().splitlines()
            sequence = "".join(lines[1:])
            dna.append(list(sequence))
    import numpy as np
    a = np.array([dna])
    a = a.squeeze(axis=0)

    c_sum = np.sum(a == 'C', axis=0)
    g_sum = np.sum(a == 'G', axis=0)
    a_sum = np.sum(a == 'A', axis=0)
    t_sum = np.sum(a == 'T', axis=0)
    arr = np.array([a_sum, c_sum, g_sum, t_sum])
    max_value = arr.max(axis=0)
    max_value = list(max_value)

    consensus = []
    x = 0
    for i in max_value:
        if i == c_sum[x]:
            consensus.append('C')
        elif i == g_sum[x]:
            consensus.append('G')
        elif i == a_sum[x]:
            consensus.append('A')
        elif i == t_sum[x]:
            consensus.append('T')
        x = x + 1
    consensus = ('').join(consensus)
    a_str = " ".join(map(str, a_sum))
    c_str = " ".join(map(str, c_sum))
    g_str = " ".join(map(str, g_sum))
    t_str = " ".join(map(str, t_sum))
    return f'{consensus}\nA: {a_str}\nC: {c_str}\nG: {g_str}\nT: {t_str}'

read_path = r'rosalind_cons.txt'
write_path = r'soliution_path_10.txt'
with open(write_path, 'w', encoding='utf-8') as outfile:
    outfile.write(consensus_profile(read_path))
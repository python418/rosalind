def mutations(x):
    with open (x) as strands:
        strands = strands.read()
        splitted = strands.splitlines()
        splitted1 = splitted[0]
        splitted2 = splitted[1]

        number = 0
        for i in range(len(splitted1)):
            if splitted1[i] != splitted2[i]:
                number = number + 1
        return number

path = r'C:\Users\yanko\OneDrive\Desktop\python_projects\rosalind\bioinformatics_stronghold\6_counting_point_mutations\rosalind_hamm.txt'
print(mutations(path))


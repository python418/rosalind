def GC(x):
    with open(x) as data:
        d = {}
        for line in data.read().splitlines():
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                d[current_id] = ''
            else:
                d[current_id] += line

        for value, key in d.items():
            d[value] = (key.count('C') + key.count('G'))/len(key) * 100

        for key, value in d.items():
            if value == max(d.values()):
                return f'{key}\n{round(value, 6)}'


path = r"rosalind_gc.txt"
print(GC(path))



        




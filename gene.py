class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        return gc / len(self.sequence) * 100

    def reverse(self):
        return self.sequence[::-1]

    def reverse_complement(self):
        rev = self.sequence[::-1]
        result = ""
        for base in rev:
            if base == "A":
                result += "T"
            elif base == "T":
                result += "A"
            elif base == "G":
                result += "C"
            elif base == "C":
                result += "G"
        return result


def load_genes(filename):
    genes = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                genes.append(Gene(parts[0], parts[1]))
    except FileNotFoundError:
        print("File not found")
    return genes


def summary(genes):
    total = 0
    best = genes[0]
    for g in genes:
        total = total + g.gc_content()
        if g.gc_content() > best.gc_content():
            best = g
    print("Genes:", len(genes))
    print("Average GC:", total / len(genes))
    print("Highest GC:", best.name)


genes = load_genes("genes.txt")
if genes:
    summary(genes)
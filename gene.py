class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        return gc / len(self.sequence) * 100
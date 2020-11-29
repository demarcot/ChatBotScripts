import random

class Deck:
    _READY = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", 
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", 
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", 
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]

    ready = _READY[:]
    table = []
    inUse = []
    burned = []

    def __init__(self):
        return

    def __str__(self):
        return ' '.join(self.ready)

    def resetDeck(self):
        self.ready = self._READY[:]
        self.burned = []
        self.inUse = []

    def flipCard(self):
        self.table.append(self._pullRandCard())

    def dealCard(self):
        c = self._pullRandCard()
        self.inUse.append(c)
        return c

    def burn(self):
        self.burned.append(self._pullRandCard())

    def _pullRandCard(self):
        i = random.randint(0, len(self.ready) - 1)
        r = self.ready.pop(i)
        return r
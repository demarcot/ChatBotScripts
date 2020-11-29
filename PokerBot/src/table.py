from deck import Deck

class Table:
    deck = Deck()
    players = []
    isHand = False

    def __init__(self):
        return
    
    def __str__(self):
        return "Players seated: " + self.players + ", Is active hand: " + self.isHand

    def openTable(self):
        self.deck.resetDeck()
        self.players = []
        print("The table is now accepting buyins.")
        return
    
    def dealHand(self):
        self.deck.resetDeck()
        for i in range(2):
            for p in self.players:
                p.append(self.deck.dealCard())
        
        return

    def addPlayer(self, player):
        self.players.append(player)
        return

    def removePlayer(self):
        return

    def getPlayer(self):
        return
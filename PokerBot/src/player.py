

class Player:
    inHand = True


    def __init__(self, name, chips, hand):
        self.name = name
        self.chips = chips
        self.hand = hand
        return

    def __str__(self):
        return '{"name": ' + self.name + ', "chips": ' + str(self.chips) + ', "hand": ' + str(self.hand) + '}'
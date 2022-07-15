class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

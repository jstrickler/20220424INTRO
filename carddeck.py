import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        # Card('rank', 'suit')
        return f"Card('{self.rank}', '{self.suit}')"


class CardDeck:  # parent: object
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer = dealer  # "private"
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.CLUB, self.DIAMOND, self.HEART, self.SPADE:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    # getter method
    def get_dealer(self):
        return self._dealer

    # getter property
    @property
    def dealer(self):
        # look up dealer ID in database
        return self._dealer

    # dealer = property(dealer)

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"<{my_name}-{self.dealer}-{len(self)}>"


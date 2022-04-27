from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck() # search parents
        joker1 = Card('JOKER', "")
        joker2 = Card('JOKER', "")
        self._cards.append(joker1)
        self._cards.append(joker2)


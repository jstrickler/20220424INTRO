from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Srini")
d2 = CardDeck("Sam")

print(d1)
print(d2)

print(d1.get_dealer())

print(d1.dealer)
print(type(d1.dealer))

d1.dealer = "Fred"
print(d1.dealer)

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
print()
print(d1.cards[0])
print()
for _ in range(5):
    print(d1.draw())
print()
print('-' * 60)
j1 = JokerDeck("Abby")
j1.shuffle()
print(j1.cards)
print(d1, j1)

print(len(d1), len(j1))






actor = "Chris Hemsworth"

x = actor.upper()
print("x: {}".format(x))
print("actor: {}".format(actor))
print(actor.count('h'))
print(actor.count('H'))

owner = "Fred"   # str name = new str("Fred");

print(actor.lower().count('h'))

print("actor.startswith('Chris'): {}".format(actor.startswith('Chris')))
print("actor.startswith('Liam'): {}".format(actor.startswith('Liam')))

#  S.startwith("value")
#  S.endswith("value")

print("'worth' in actor: {}".format('worth' in actor))
print("'is' in actor: {}".format('is' in actor))
print("'wombat' in actor: {}".format('wombat' in actor))

print("actor.find('worth'): {}".format(actor.find('worth')))

s = "     I love Python!     "
print("|" + s + "|")
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

raw_line = "spam\n"
line = raw_line.rstrip()  # remove \n

data = "     Joe    Blow Houston\tTX     "
fields = data.split()
print("fields: {}".format(fields))


s = "xyyyyxxxyyxyyxyyxyxThe happy glow of a wax candleyyyyyyyx"
print("|" + s + "|")
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()




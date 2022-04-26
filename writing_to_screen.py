person = "Thor"
city = "Asgard"
value = 38.439034902293

print(person, city, value)
# output str(person) + ' ' + str(person) + ' ' + str(value) + '\n'

print("next...")

print(person)
print(city)
print(value)

print(person, end="/")
print(city, end=": ")
print(value)

print(person, city, value, sep="/")
print(person, city, value, sep="#")
print(person, city, value, sep="")
print(person, city, value, sep=" -- ")
print()

s = f"{person} lives in {city}"  # f-string (available in 3.6 and later)
print("s: {}".format(s))

#    0           1            0       1
s = "{} lives in {}".format(person, city)
print("s: {}".format(s))

print(f"Value is {value}")
print(f"Value is {value:.2f}")
print("Value is {:.2f}".format(value))

x = 39287293872062760296702972602760
print(f"x is {x:,d}")

print("%s lives in %s" % (person, city))
print("Value is %.2f" % (value))




#  print(item1, item2, ..., sep="sep char", end="end char")

counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()

for food in foods:
    if food in counts:
        counts[food] += 1
    else:
        counts[food] = 1

for food, count in counts.items():
    print(food, count)


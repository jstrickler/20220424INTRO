
cities = ['Mumbai', 'Hyderabad', 'Chennai',
          'Jalpur', 'Lucknow', 'Kolkata', 'Delhi']

for test_value in 'Chennai', 'Pune', 'Hyderabad', 'Delhi':
    print(test_value, test_value in cities)
print()

del cities[-1]
print("cities: {}".format(cities))

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']
result = x + y
print("result: {}".format(result))

w = 'wombat'
wombats = w * 3
print("wombats: {}".format(wombats))

flags = [False] * 10
print("flags: {}".format(flags))

print('-' * 60)


print(len(cities), min(cities), max(cities), sorted(cities))
print('-' * 60)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()

print("cities: {}".format(cities))

rev_cities = reversed(cities)
print("rev_cities: {}".format(rev_cities))
for city in rev_cities:
    print(city)
print()
print(type(rev_cities))  # generator

rev_cities = reversed(cities)
reversed_cities = list(rev_cities)
print("reversed_cities: {}".format(reversed_cities))

r2 = list(rev_cities)
print("r2: {}".format(r2))

pops = [12442373, 6809970, 4681087, 3046163, 2815601, 4486679]

city_pops = zip(cities, pops)
print(city_pops, '\n')

for city, population in city_pops:
    print(f"{city:10s} {population:8d}")
print()

city_pops = zip(cities, pops)
print(list(city_pops))
print()

for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)), '\n')

i = 0
while i < 5:
    print(i)
    i += 1
print()

for i in range(5):
    print(i)
print()

#  range(stop)   range(start, stop)  range(start, stop, step)

for i in range(1, 6):
    print(i, end=' ')
print('\n')










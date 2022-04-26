list1 = list()   # empty list
list2 = ['lemon', 'mango', 'papaya', 'apple']
print(list2[0])
list3 = []  # empty list
s = "wombat kangaroo quokka"
animals = s.split()
print(animals)

cities = ['Mumbai', 'Hyderabad', 'Chennai',
          'Jalpur', 'Lucknow']

print(cities[0], cities[4])
cities.insert(0, 'Kolkata')
print("cities: {}".format(cities))
cities.insert(3, 'Pune')
print("cities: {}".format(cities))
cities.append('Surat')
cities.append('Ahmedabad')
print("cities: {}".format(cities))

more_cities = ['Bangalore', 'Delhi', 'Kanpur']
cities.extend(more_cities)
print("cities: {}".format(cities))

#  LIST.insert(pos, value)
#  LIST.append(value)
#  LIST.extend(iterable)

cities[3] = 'Patna'
print("cities: {}".format(cities))

del cities[4]
print("cities: {}".format(cities))

cities.remove('Ahmedabad')
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(5)
print("city: {}".format(city))
print("cities: {}".format(cities))

# del LIST[pos]   LIST.remove(value)
# x = LIST.pop()  x = list.pop(pos)
print("len(cities): {}".format(len(cities)))

print(cities[0], cities[5], cities[7])
print(cities[len(cities)-1])
print(cities[-1], cities[-0], '\n')

person = "Bill Gates"
print(person[0], person[7], person[-1], person[-2], '\n')
for letter in person:
    print(letter)
print()

print("cities[0:4]: {}".format(cities[0:4]))

#  LIST[start:stop]   [:stop]  [start:]  [:]
print("cities[5:8]: {}".format(cities[5:8]))  # [5] to [7]
print("cities[:]: {}".format(cities[:]))  # all elements
print("cities[6:]: {}".format(cities[6:]))  # [6] to end
print("cities[-3:]: {}".format(cities[-3:]))  # last 3
print('-' * 60)

# for VAR in ITERABLE:
#    ...

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)

#  Bungalow
print("cities: {}".format(cities))

print("','.join(cities): {}".format(','.join(cities)))
print(' '.join(cities))
print('#'.join(cities))
print(' -- '.join(cities))

"""
struct {
    char *fname;
    char *lname;
    int age;
}
"""
















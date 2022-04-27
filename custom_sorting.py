fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

def ignore_case(s):
    comparison_value =  s.lower()
    print(f"comparing {s} as {comparison_value}")
    return comparison_value

f1 = sorted(fruits, key=ignore_case)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def my_sort(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=my_sort)
print("f4: {}\n".format(f4))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = sorted(nums)
print("n1: {}\n".format(n1))

n2 = sorted(nums, key=str)
print("n2: {}\n".format(n2))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):  # not sordid
    print(person)
print('-' * 60)

def by_dob(p):
    return p[3]   # or p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

print("\U0001F92F")

def by_last_first_name(p):
    return p[1], p[0]

for person in sorted(people, key=by_last_first_name):
    print(person)
print('-' * 60)


for person in sorted(people, key=lambda p: (p[1], p[0])):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports.items(), '\n')

def by_value(item):
    return item[1], item[0]   # sort by value, then key

for code, name in sorted(airports.items(), key=by_value, reverse=True):
    print(code, name)
print('-' * 60)

print("fruits: {}\n".format(fruits))
fruits.sort(key=str.lower)
print("fruits: {}\n".format(fruits))





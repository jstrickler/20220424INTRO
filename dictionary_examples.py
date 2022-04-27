
d1 = dict()  # empty dict
d2 = {'m': 9, 'k': 13, 'r': 4, 'a': 19}
d3 = {}  # empty dict

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

print(airports['RDU'])
airports['MIA'] = 'Miami'
airports['BOM'] = 'Mumbai'
print("airports: {}".format(airports))
print("airports['EWR']: {}".format(airports['EWR']))
# print("airports['MAA']: {}".format(airports['MAA']))

print("airports.get('MAA'): {}".format(airports.get('MAA')))
print("airports.get('MAA', 0): {}".format(airports.get('MAA', 0)))

for code in 'ABQ', 'MAA', 'MIA', 'MCO', 'JFK':
    print(code, code in airports)
print()

del airports['EWR']
print("airports: {}".format(airports))

airports['RDU'] = 'Durham'

print("airports: {}".format(airports))

print("len(airports): {}".format(len(airports)))

print(airports.get('MAA'))

print(airports.setdefault('MAA', 'Chennai'))
print("airports: {}".format(airports))

print(airports.items())
print('-' * 60)
for code, city in sorted(airports.items()):
    print(code, city)
print()









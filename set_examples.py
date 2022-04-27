srini_countries = ['Laos', 'Australia', 'Mozambique', 'Laos', 'Laos', 'Japan',
                   'Malaysia', 'US', 'Canada', 'US', 'US', 'US']

mary_countries = ['US', 'Laos', 'Japan', 'Germany', 'Iceland', 'Russia',
                  'Uruguay', 'Canada']

srini = set(srini_countries)
mary = set(mary_countries)
mary.add('Mozambique')

print("COMMON:", srini & mary)  # intersection
print("NOT COMMON:", srini ^ mary)  # xor
print("BOTH:", srini | mary)  # union
print("ONLY Srini:", srini - mary)
print("ONLY Mary:", mary - srini)


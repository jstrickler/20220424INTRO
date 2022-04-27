import json
from pprint import pprint


with open('DATA/presidents.json') as presidents_in:
    president_data = json.load(presidents_in)

president_list = president_data['presidents']
for president in president_list:
    print(president['firstname'], president['lastname'])
print('-' * 60)
pprint(president_list)

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

with open('computer_people.json', 'w') as cp_out:
    json.dump(people, cp_out, indent=4)



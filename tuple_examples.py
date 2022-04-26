
# () are redundant
person = ('Bill', 'Gates', 'Microsoft', '1955-10-28')

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'
print(person[0], person[1])


first_name, last_name, product, dob = person  # iterable unpacking

# to get field names a la  person.first_name, person.last_name, etc., use
# namedtuple
# dataclass
# normal class

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('John', 'Strickler', '1962-08-17'),
]

print("type(people): {}".format(type(people)))
print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))
print()

for person in people:
    # unpack here??
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # ...
    print(first_name, last_name, product)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


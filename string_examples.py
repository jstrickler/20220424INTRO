s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
s = "m"

print("len(s1): {}".format(len(s1)))
print("len(s5): {}".format(len(s5)))

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")


query = """
select first_name, last_name
from customers
where last_name like 'str';
"""


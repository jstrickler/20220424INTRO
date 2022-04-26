fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#    [expr for var1, var2, ... in iterable]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f4 = [f.title() for f in fruits if f.startswith('p') if len(f) > 5]
print("f4: {}\n".format(f4))


powers = [(i, i ** 2, i **3) for i in range(10)]
print("powers: {}\n".format(powers))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n1 = [float(n) * 10 for n in nums if n > 300]
print("n1: {}\n".format(n1))


fruits_gen = (f.upper() for f in fruits if f.startswith('a'))
print("fruits_gen: {}\n".format(fruits_gen))
for fruit in fruits_gen:
    print(fruit)


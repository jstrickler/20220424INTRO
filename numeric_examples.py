# int float

# integers
i1 = 1234
i2 = -1234
i3 = 0
i4 = 3226236526293865295862937659826395826395862395862938562
i5 = 2_390_930

# hex
i4 = 0xDeadBeef

# binary
i5 = 0b10011001

# floats
f1 = 123.456
f2 = 123.
f3 = .456
f4 = 0.456
f5 = -4.2903923432

a = 23
b = 5
print(a + b, a - b)
print(a * b, a / b, a / -b, a // b, a // -b)
print(a ** b, a % b)

c = -5
print(-c)

x = 5
x += 10  # x = x + 10
x *= 4   # x = x * 4
x /= 3   # etc
print("x: {}".format(x))


#  x++, x--, ++x, --x   NOT SUPPORTED

r = 25
t = 0
# print(r / t) can't divide by zero

a = 123
b = "456"
print(a + int(b))
print(str(a) + b)







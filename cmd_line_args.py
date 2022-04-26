import sys   # run-time info

print("sys.argv: {}".format(sys.argv))

print("sys.argv[0]: {}".format(sys.argv[0]))
print("sys.argv[1]: {}".format(sys.argv[1]))

number = float(sys.argv[1])
print(f"The square root of {number} is {number ** .5}")

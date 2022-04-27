
x = 25  # global


def spam(user_name):
    # global x  Very Bad Thing!!
    x = 1000
    color = "green"  # local name
    print("in spam: x is", x)
    print("user name is", user_name)

spam("Waldo")
print("in main: x is", x)

# local -> global -> builtin






i = 0
while i < 3:  # see range() class
    print(i)
    i += 1
print()

while True:
    user_name = input("User name (or q to quit): ")
    if user_name == 'q':
        break  # exit loop

    birth_state = input("Birth state: ")
    if (user_name == '') or (birth_state == ''):
        print("please enter name and state")
        continue  # go back to top

    print(f"{user_name} is from {birth_state}")


while True:
    print("yikes!!")

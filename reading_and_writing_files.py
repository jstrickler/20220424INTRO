file_path = "DATA/mary.txt"

mary_in = open(file_path, "r")
# process file here ...
mary_in.close()


with open(file_path) as mary_in:
    pass

with open(file_path) as mary_in:
    for raw_line in mary_in:  # read one line at a time
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    all_text = mary_in.read()   # read entire file into str
    print("RAW:")
    print(repr(all_text))
    print("NORMAL:")
    print(all_text)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    all_lines = contents.splitlines()
    print(all_lines)
print('-' * 60)

with open('DATA/tyger.txt') as tyger_in:
    for raw_line in tyger_in:
        if 'Tyger' in raw_line:
            line = raw_line.rstrip()
            print(line)
print('-' * 60)

target = 'x'
count = 0
output_file_name = f"{target}_words.txt"
with open('DATA/words.txt') as words_in:
    with open(output_file_name, 'w') as words_out:
        for raw_line in words_in:
            if raw_line.startswith(target):
                count += 1
                words_out.write(raw_line)

print(f"{count} words start with '{target}'")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit + '\n')


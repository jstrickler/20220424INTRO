from math import pi
import os

def hello():
    print("Hello, DELL world")

hello()

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

a1 = circle_area(10)
print("a1: {}".format(a1))

print(circle_area(2))

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 10))


def greet(whom="world"):
    print("Hello,", whom)

greet('Mom')
greet("Baby sister")
greet()

def find_term(search_term, *file_paths):
    found_lines = []
    for file_path in file_paths:
        base_name = os.path.basename(file_path)
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    found_lines.append(raw_line.rstrip())
    return found_lines

lines = find_term('pig', 'DATA/alice.txt', 'DATA/words.txt', 'DATA/parrot.txt')
print(lines, '\n')



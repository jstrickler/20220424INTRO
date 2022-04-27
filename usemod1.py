#  find and run geometry.py
from john.math import geometry
import sys

# module.name
a = geometry.circle_area(10)
print("a: {}".format(a))

geometry._spam()

# module search algorithm
# 1. current folder
# 2. folders in PYTHONPATH
# 3. install folder
for path in sys.path:
    print(path)


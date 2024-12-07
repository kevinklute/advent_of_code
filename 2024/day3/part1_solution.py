import sys
import re

filename = sys.argv[1]
total = 0

with open(filename) as file:
    muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', file.read(), re.DOTALL)
for mul in muls:
    total += int(mul[0]) * int(mul[1])
print(total)

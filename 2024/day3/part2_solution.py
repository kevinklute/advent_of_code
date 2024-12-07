import sys
import re

filename = sys.argv[1]
total = 0

with open(filename) as file:
    muls = re.findall(r'(?:don\'t\(\).*?(?:\Z|do\(\)))|(?:mul\((\d{1,3}),(\d{1,3})\))', file.read(), re.DOTALL)
for mul in muls:
    if mul[0] != '':
        total += int(mul[0]) * int(mul[1])
print(total)

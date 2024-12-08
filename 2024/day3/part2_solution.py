import sys
import re

filename = sys.argv[1]
with open(filename) as file:
    muls = re.findall(r'(?:don\'t\(\).*?(?:\Z|do\(\)).*?)*mul\((\d{1,3}),(\d{1,3})\)', file.read(), re.DOTALL)
print(sum(map(lambda m: int(m[0]) * int(m[1]), muls)))

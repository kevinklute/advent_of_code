import sys
import re

filename = sys.argv[1]
total = 0
words = []
flattened = []

with open(filename) as file:
    for line in file:
        words.append(list(line.strip('\n')))

for row in words:
    flattened.append(''.join(row))
for j in range(len(words)):
    flattened.append(''.join([words[i][j] for i in range(len(words))]))
for start_row in range(-1 * len(words), 2 * len(words)):
    word = ''
    for x in range(len(words)):
        i, j = start_row + x, x
        if 0 <= i < len(words) and 0 <= j < len(words):
            word += words[i][j]
    if word != '':
        flattened.append(word)
    word = ''
    for x in range(len(words)):
        i, j = start_row - x, x
        if 0 <= i < len(words) and 0 <= j < len(words):
            word += words[i][j]
    if word != '':
        flattened.append(word)

for candidate in flattened:
    total += len(re.findall(r'XMAS', candidate))
    total += len(re.findall(r'SAMX', candidate))
        
print(total)

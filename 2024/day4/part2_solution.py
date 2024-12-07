import sys
import re

filename = sys.argv[1]
total = 0
words = []

with open(filename) as file:
    for line in file:
        words.append(list(line.strip('\n')))

for i in range(len(words) - 2):
    for j in range(len(words) - 2):
        word1 = words[i][j] + words[i + 1][j + 1] + words[i + 2][j + 2]
        word2 = words[i + 2][j] + words[i + 1][j + 1] + words[i][j + 2]
        if word1 in ['MAS', 'SAM'] and word2 in ['MAS', 'SAM']:
            total += 1
        
print(total)

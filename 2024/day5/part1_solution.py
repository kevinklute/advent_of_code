import sys
import re

filename = sys.argv[1]
total = 0
rules = []
updates = []

with open(filename) as file:
    for line in file:
        if '|' in line:
            before, after = line.strip('\n').split('|')
            rules.append(re.compile(after + '.*' + before))
        elif ',' in line:
            updates.append(line)

for update in updates:
    correct = True
    for rule in rules:
        if re.search(rule, update):
            correct = False
            break
    if correct:
        pages = update.split(',')
        total += int(pages[int(len(pages) / 2)])

print(total)

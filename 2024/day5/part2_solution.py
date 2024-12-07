import sys
import re

filename = sys.argv[1]
total = 0
rules = []
rule_nums = []
updates = []
incorrects = []

with open(filename) as file:
    for line in file:
        if '|' in line:
            before, after = line.strip('\n').split('|')
            rule_nums.append((before, after))
            rules.append(re.compile(after + '.*' + before))
        elif ',' in line:
            updates.append(line)

for update in updates:
    correct = True
    for rule in rules:
        if re.search(rule, update):
            correct = False
            continue
    if not correct:
        incorrects.append(update)

for j in range(len(incorrects)):
    correct = False
    while not correct:
        correct = True
        update = incorrects[j]
        for i in range(len(rules)):
            if re.search(rules[i], update):
                correct = False
                (before, after) = rule_nums[i]
                segments = re.split(re.compile(before + '|' + after), update)
                incorrects[j] = segments[0] + before + segments[1] + after + segments[2]

for update in incorrects:
    pages = update.split(',')
    total += int(pages[int(len(pages) / 2)])

print(total)

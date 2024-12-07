import sys

filename = sys.argv[1]
list1 = []
freq_table = {}
score = 0

with open(filename) as file:
    for line in file:
        elements = line.split('   ')
        list1.append(int(elements[0]))
        element1 = int(elements[1])
        if element1 not in freq_table:
            freq_table[element1] = 0
        freq_table[element1] += 1

for x in list1:
    if x in freq_table:
        score += (x * freq_table[x])

print(score)

import sys

filename = sys.argv[1]
list1, list2 = [], []
total_dist = 0

with open(filename) as file:
    for line in file:
        elements = line.split('   ')
        list1.append(int(elements[0]))
        list2.append(int(elements[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    total_dist += abs(list1[i] - list2[i])

print(total_dist)

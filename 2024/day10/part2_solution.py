import sys

filename = sys.argv[1]
topo = []
with open(filename) as file:
    for line in file:
        topo.append([int(c) for c in line.strip('\n')])

def search(x, y):
    if topo[y][x] == 9:
        return 1 
    target = topo[y][x] + 1
    output = 0
    if y + 1 < len(topo) and topo[y + 1][x] == target:
        output += search(x, y + 1)
    if y - 1 >= 0 and topo[y - 1][x] == target:
        output += search(x, y - 1)
    if x + 1 < len(topo[0]) and topo[y][x + 1] == target:
        output += search(x + 1, y)
    if x - 1 >= 0 and topo[y][x - 1] == target:
        output += search(x - 1, y)
    return output

trails = 0
for y in range(len(topo)):
    for x in range(len(topo[0])):
        if topo[y][x] == 0:
            trails += search(x, y)
print(trails)

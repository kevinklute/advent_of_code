import sys

filename = sys.argv[1]
plant_map = []
with open(filename) as file:
    for line in file:
        plant_map.append(list(line.strip('\n')))

plots = [[(x, y) for x in range(len(plant_map[y]))] for y in range(len(plant_map))]

def union(loc1, loc2):
    rep1 = find(loc1)
    rep2 = find(loc2)
    if rep1 != rep2:
        plots[rep1[1]][rep1[0]] = rep2

def find(loc):
    if loc == plots[loc[1]][loc[0]]:
        return loc
    return find(plots[loc[1]][loc[0]])

for y in range(len(plant_map)):
    for x in range(len(plant_map[y])):
        if x + 1 < len(plant_map[0]) and plant_map[y][x] == plant_map[y][x + 1]:
            union((x, y), (x + 1, y))
        if x - 1 >= 0 and plant_map[y][x] == plant_map[y][x - 1]:
            union((x, y), (x - 1, y))
        if y + 1 < len(plant_map) and plant_map[y][x] == plant_map[y + 1][x]:
            union((x, y), (x, y + 1))
        if y - 1 >= 0 and plant_map[y][x] == plant_map[y - 1][x]:
            union((x, y), (x, y - 1))

prices = {}
for y in range(len(plant_map)):
    for x in range(len(plant_map[y])):
        edges = []
        if not (x + 1 < len(plant_map[0]) and plant_map[y][x] == plant_map[y][x + 1]):
            edges.append((x, y, 'e'))
        if not (x - 1 >= 0 and plant_map[y][x] == plant_map[y][x - 1]):
            edges.append((x, y, 'w'))
        if not (y + 1 < len(plant_map) and plant_map[y][x] == plant_map[y + 1][x]):
            edges.append((x, y, 's'))
        if not (y - 1 >= 0 and plant_map[y][x] == plant_map[y - 1][x ]):
            edges.append((x, y, 'n'))
        parent = find((x, y))
        if parent not in prices:
            prices[parent] = (0, [])
        prices[parent] = (prices[parent][0] + 1, prices[parent][1] + edges)

class EdgeUnionFind:
    def __init__(self, size):
        self.parents = list(range(size))
    def union(self, x, y):
        rep1 = self.find(x)
        rep2 = self.find(y)
        if rep1 != rep2:
            self.parents[rep1] = rep2
    def find(self, x):
        if x == self.parents[x]:
            return x
        return self.find(self.parents[x])

total = 0
for key in prices:
    perimeter = 0
    edges = prices[key][1]
    uf = EdgeUnionFind(len(edges))
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            (x1, y1, d1) = edges[i]
            (x2, y2, d2) = edges[j]
            if (x1 + 1, y1, d1) == (x2, y2, d2) or (x1, y1 + 1, d1) == (x2, y2, d2):
                uf.union(i, j)
    sides = set()
    for parent in uf.parents:
        sides.add(uf.find(parent))
    total += prices[key][0] * len(sides)
print(total)


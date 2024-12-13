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
        perimeter = 4
        if x + 1 < len(plant_map[0]) and plant_map[y][x] == plant_map[y][x + 1]:
            perimeter -= 1
        if x - 1 >= 0 and plant_map[y][x] == plant_map[y][x - 1]:
            perimeter -= 1
        if y + 1 < len(plant_map) and plant_map[y][x] == plant_map[y + 1][x]:
            perimeter -= 1
        if y - 1 >= 0 and plant_map[y][x] == plant_map[y - 1][x ]:
            perimeter -= 1
        parent = find((x, y))
        if parent not in prices:
            prices[parent] = (0, 0)
        prices[parent] = (prices[parent][0] + 1, prices[parent][1] + perimeter)

total = 0
for key in prices:
    total += prices[key][0] * prices[key][1]
print(total)

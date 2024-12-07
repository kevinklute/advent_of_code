import sys
import copy

filename = sys.argv[1]
grid = []

with open(filename) as file:
    for line in file:
        grid.append(list(line.strip('\n')))

def turn_right(vector):
    if vector == (-1, 0):
        return (0, 1)
    elif vector == (0, 1):
        return (1, 0)
    elif vector == (1, 0):
        return (0, -1)
    else:
        return (-1, 0)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            position = (i, j)
            start_pos = position

vector = (-1, 0)
candidates = set() 
while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
    old_pos = position
    position = (position[0] + vector[0], position[1] + vector[1])
    if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]) and grid[position[0]][position[1]] == '#':
        position = old_pos
        vector = turn_right(vector)
    elif 0 <= old_pos[0] < len(grid) and 0 <= old_pos[1] < len(grid[0]) and old_pos != start_pos:
        candidates.add(old_pos)

total = 0
for candidate in candidates:
    visited = {}
    grid[candidate[0]][candidate[1]] = '#'
    position = start_pos
    vector = (-1, 0)
    while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
        if position in visited and visited[position] == vector:
            total += 1;
            break;
        i += 1
        old_pos = position
        position = (position[0] + vector[0], position[1] + vector[1])
        if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]) and grid[position[0]][position[1]] == '#':
            position = old_pos
            vector = turn_right(vector)
        elif 0 <= old_pos[0] < len(grid) and 0 <= old_pos[1] < len(grid[0]):
            visited[old_pos] = vector
    grid[candidate[0]][candidate[1]] = '.'

print(total)

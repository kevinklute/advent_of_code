import sys
import re

filename = sys.argv[1]
grid = []

with open(filename) as file:
    for line in file:
        grid.append(list(line.strip('\n')))

position = (0, 0)
vector = (-1, 0)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            position = (i, j)

while 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]):
    old_pos = position
    position = (position[0] + vector[0], position[1] + vector[1])
    if 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0]) and grid[position[0]][position[1]] == '#':
        # Walked into a wall - step back and turn right
        position = old_pos
        if vector == (-1, 0):
            vector = (0, 1)
        elif vector == (0, 1):
            vector = (1, 0)
        elif vector == (1, 0):
            vector = (0, -1)
        else:
            vector = (-1, 0)
    elif 0 <= old_pos[0] < len(grid) and 0 <= old_pos[1] < len(grid[0]):
        # Mark last position as visited
        grid[old_pos[0]][old_pos[1]] = 'X'

            
total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            total += 1
print(total)

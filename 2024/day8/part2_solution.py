import sys
import math

filename = sys.argv[1]

antenna_map = {}
width, height = 0, 0
with open(filename) as file:
    for i, line in enumerate(file):
        height = max(i + 1, height)
        for j, node in enumerate(line.strip('\n')):
            width = max(j + 1, width)
            if node != '.':
                if node not in antenna_map:
                    antenna_map[node] = []
                antenna_map[node].append((j, i))
antinodes = set()
for frequency in antenna_map:
    antennas = antenna_map[frequency]
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            antenna1 = antennas[i]
            antenna2 = antennas[j]
            unsimplified_vector = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
            divisor = math.gcd(unsimplified_vector[0], unsimplified_vector[1])
            vector = (unsimplified_vector[0] / divisor, unsimplified_vector[1] / divisor)
            antinode = antenna1
            while 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                antinodes.add(antinode)
                antinode = (antinode[0] - vector[0], antinode[1] - vector[1])
            antinode = antenna2
            while 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                antinodes.add(antinode)
                antinode = (antinode[0] + vector[0], antinode[1] + vector[1])
print(len(antinodes))

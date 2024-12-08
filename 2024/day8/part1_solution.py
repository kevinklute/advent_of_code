import sys

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
            vector = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
            antinode1 = (antenna1[0] - vector[0], antenna1[1] - vector[1])
            antinode2 = (antenna2[0] + vector[0], antenna2[1] + vector[1])
            if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                antinodes.add(antinode1)
            if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                antinodes.add(antinode2)
print(len(antinodes))

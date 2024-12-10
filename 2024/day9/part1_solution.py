import sys

filename = sys.argv[1]

with open(filename) as file:
    disk_map = [int(c) for c in file.read().strip('\n')]

disk_index, map_index = 0, 0
map_len = len(disk_map)
# trim trailing free block
if map_len % 2 == 0:
    map_len -= 1
checksum = 0
while map_index < map_len:
    # file block
    if map_index % 2 == 0:
        for i in range(disk_map[map_index]):
            checksum += disk_index * int((map_index + 1) / 2)
            disk_index += 1
    # free block
    else:
        for i in range(disk_map[map_index]):
            while disk_map[map_len - 1] == 0:
                map_len -= 2
            if map_index >= map_len:
                break
            checksum += disk_index * int(map_len / 2)
            disk_map[map_len - 1] -= 1
            disk_index += 1
    map_index += 1
print(checksum)


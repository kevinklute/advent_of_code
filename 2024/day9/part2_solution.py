import sys

filename = sys.argv[1]

with open(filename) as file:
    disk_map = [int(c) for c in file.read().strip('\n')]

disk = []
for map_index, digit in enumerate(disk_map):
    for i in range(digit):
        if map_index % 2 == 0:
            disk.append(int(map_index / 2))
        else:
            disk.append('.')

file_index_to_move = len(disk) - 1
memo = {}
while file_index_to_move > 0:
    file_to_move = disk[file_index_to_move]
    if file_to_move != '.':
        file_size = 0
        i = file_index_to_move
        while file_index_to_move > 0 and disk[file_index_to_move] == file_to_move:
            file_size += 1
            file_index_to_move -= 1
        file_index_to_move += 1
        i = 0
        free_index = -1
        while i < file_index_to_move:
            free_size = 0
            free_index = i
            if disk[i] == '.':
                if i in memo:
                    free_size += memo[i]
                    i += memo[i]
                else:
                    while disk[i] == '.':
                        free_size += 1
                        i += 1
                    memo[free_index] = free_size
            else:
                if i in memo:
                    i += memo[i]
                else:
                    non_free_index = i
                    non_free_size = 0
                    while i < file_index_to_move and disk[i] != '.':
                        i += 1
                        non_free_size += 1
                    memo[non_free_index] = non_free_size
            if file_size <= free_size:
                for i in range(file_size):
                    disk[free_index + i] = file_to_move
                    disk[file_index_to_move + i] = '.'
                if free_index in memo:
                    del memo[free_index]
                break
    file_index_to_move -= 1

checksum = 0
for file_index, file_id in enumerate(disk):
    if file_id != '.':
        checksum += file_index * file_id
print(checksum)

import sys

filename = sys.argv[1]
stones = []
with open(filename) as file:
    stones = [int(s) for s in file.read().strip('\n').split(' ')]
for r in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        str_stone = str(stone)
        if stone == 0:
            stones[i] = 1
        elif len(str_stone) % 2 == 0:
            new_stone_1 = int(str_stone[:int(len(str_stone) / 2)])
            new_stone_2 = int(str_stone[int(len(str_stone) / 2):])
            stones[i] = new_stone_1
            i += 1
            stones.insert(i, new_stone_2)
        else:
            stones[i] = stone * 2024
        i += 1
print(len(stones))

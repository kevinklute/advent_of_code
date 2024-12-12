import sys
import math

filename = sys.argv[1]
num_rounds = int(sys.argv[2])
with open(filename) as file:
    stones = [int(s) for s in file.read().strip('\n').split(' ')]

memo = {}
def count_stones(rounds, stone):
    if (rounds, stone) in memo:
        return memo[(rounds, stone)]
    stone_size = int(math.log10(stone)) + 1 if stone > 0 else 0
    if rounds == 0:
        out = 1
    elif stone == 0:
        out = count_stones(rounds - 1, 1) 
    elif stone_size % 2 == 0:
        out = count_stones(rounds - 1, int(stone / (10 ** (stone_size / 2)))) + count_stones(rounds - 1, int(stone % (10 ** (stone_size / 2))))   
    else:
       out = count_stones(rounds - 1, stone * 2024) 
    memo[(rounds, stone)] = out
    return out

total = 0
for stone in stones:
    total += count_stones(num_rounds, stone)
print(total)

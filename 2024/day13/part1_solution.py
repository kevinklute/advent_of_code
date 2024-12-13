import sys
import re

a_cost, b_cost = 3, 1
max_cost = 3 * 100 + 100 + 1

filename = sys.argv[1]
with open(filename) as file:
    puzzles = re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)', file.read(), re.DOTALL)

total_cost = 0
for puzzle in puzzles:
    a_x_str, a_y_str, b_x_str, b_y_str, prize_x_str, prize_y_str = puzzle
    a_x, a_y, b_x, b_y, prize_x, prize_y = int(a_x_str), int(a_y_str), int(b_x_str), int(b_y_str), int(prize_x_str), int(prize_y_str)
    best = max_cost
    for a_count in range(100):
        for b_count in range(100):
            x = a_x * a_count + b_x * b_count
            y = a_y * a_count + b_y * b_count
            cost = a_cost * a_count + b_cost * b_count
            if (x, y) == (prize_x, prize_y):
                best = min(best, cost)
    if best < max_cost:
        total_cost += best
print(total_cost)

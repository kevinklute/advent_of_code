import sys
import re
import scipy.optimize
import numpy as np

a_cost, b_cost = 3, 1

filename = sys.argv[1]
with open(filename) as file:
    puzzles = re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)', file.read(), re.DOTALL)

total_cost = 0
for puzzle in puzzles:
    a_x_str, a_y_str, b_x_str, b_y_str, prize_x_str, prize_y_str = puzzle
    a_x, a_y, b_x, b_y, prize_x, prize_y = int(a_x_str), int(a_y_str), int(b_x_str), int(b_y_str), int(prize_x_str), int(prize_y_str)
    prize_x += int(sys.argv[2])
    prize_y += int(sys.argv[2])
    minimization_function = [-1 * a_cost, -1 * b_cost]
    equations_lhs = [[a_x, b_x], [a_y, b_y]]
    equations_rhs = [prize_x, prize_y]
    result = scipy.optimize.linprog(minimization_function, A_eq=equations_lhs, b_eq=equations_rhs, integrality=[1, 1])
    if result.success:
        a_count, b_count = int(result.x[0]), int(result.x[1])
        print(str(int(a_count)) + " " + str(int(b_count)))
        if prize_x != a_x * a_count + b_x * b_count or prize_y != a_y * a_count + b_y * b_count:
            print("ERROR")
        total_cost += -1 * int(result.fun)
    while prize_x > 0:
        prize_x -= a_x
print(total_cost)

import sys

filename = sys.argv[1]

equations = []
with open(filename) as file:
    for line in file:
        split1 = line.split(': ')
        split2 = split1[1].split(' ')
        equations.append((int(split1[0]), [int(n) for n in split2]))

def test(target, operands):
    if len(operands) == 2:
        return operands[0] + operands[1] == target or operands[0] * operands[1] == target
    return test(target, [operands[0] + operands[1]] + operands[2:]) or test(target, [operands[0] * operands[1]] + operands[2:])

total = sum(map(lambda e: e[0], filter(lambda e: test(e[0], e[1]), equations)))
print(total)

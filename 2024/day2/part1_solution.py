import sys

filename = sys.argv[1]
safe_count = 0

with open(filename) as file:
    for report in file:
        safe = True
        levels = [int(x) for x in report.split(' ')]
        if levels[1] > levels[0]:
            sign = 1
        elif levels[1] < levels[0]:
            sign = -1
        else:
            sign = 0
        for i in range(1, len(levels)):
            if not 1 <= ((levels[i] - levels[i - 1]) * sign) <= 3:
                safe = False
        if safe:
            safe_count += 1

print(safe_count)

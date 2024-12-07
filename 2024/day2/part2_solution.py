import sys

filename = sys.argv[1]
safe_count = 0

def get_level(levels, index, skip_index = -1):
    if skip_index == -1 or index < skip_index:
        return levels[index]
    return levels[index + 1]

def is_safe(levels, skip_index = -1):
    if get_level(levels, 1, skip_index) > get_level(levels, 0, skip_index):
        sign = 1
    elif get_level(levels, 1, skip_index) < get_level(levels, 0, skip_index):
        sign = -1
    else:
        sign = 0
    length = len(levels) if skip_index == -1 else len(levels) - 1
    for i in range(1, length):
        if not 1 <= ((get_level(levels, i, skip_index) - get_level(levels, i - 1, skip_index)) * sign) <= 3:
            if skip_index == -1:
                return is_safe(levels, i) or is_safe(levels, i - 1) or is_safe(levels, 0)
            return False
    return True

with open(filename) as file:
    for report in file:
        safe = True
        levels = [int(x) for x in report.split(' ')]
        safe_count += is_safe(levels)
    
print(safe_count)

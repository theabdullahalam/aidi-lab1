def print_pattern(lines):
    for i in range(lines, 0, -1):
        for j in range(0, i):
            print('*', end='')
        print()

print_pattern(5)
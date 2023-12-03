import re
from math import prod

soubor_s_daty = 'AdventOfCode_2023_3_day\\3_12_2023_input.txt'
# soubor_s_daty = 'test_folder\\test.txt'

with open(soubor_s_daty, 'r') as file:
    broken_schema_motor = [radek.strip() for radek in file.readlines() if radek.strip()]               

DATA = broken_schema_motor
FINDERS = [list(re.finditer(r"(\d+)", line)) for line in DATA]
ALL_SYMBOLS = {}

def find_symbol(y, match):
    for v in [y - 1, y, y + 1]:
        for u in range(match.start() - 1, match.end() + 1):
            if (
                0 <= v < len(DATA)
                and 0 <= u < len(DATA[0])
                and DATA[v][u] != "."
                and not DATA[v][u].isdigit()
            ):
                return v, u

def find_all_symbols():
    for y, line in enumerate(FINDERS):
        for match in line:
            if symbol := find_symbol(y, match):
                ALL_SYMBOLS.setdefault(symbol, []).append(int(match[1]))
        print(ALL_SYMBOLS)

find_all_symbols()

def part_one():
    return sum(sum(parts) for parts in ALL_SYMBOLS.values())

print(part_one())

def part_two():
    return sum(
        prod(parts)
        for (y, x), parts in ALL_SYMBOLS.items()
        if DATA[y][x] == "*" and len(parts) == 2
    )
    
print(part_two())
import math
from pathlib import Path
from typing import List


def calc_fuel(i: int) -> int:
    return math.floor(i / 3) - 2


def calc_new_fuel(value: int) -> int:
    return math.floor(value / 3) - 2


def calc_fuel_p2(i: int, next_fuel: int = 0) -> int:
    fuel = calc_new_fuel(i)
    if calc_new_fuel(fuel) < 1:
        yield fuel
    else:
        yield fuel + calc_fuel(next_fuel)


def read_data(filename: str) -> List[int]:
    data_file = Path(__file__).parent.parent.absolute() / 'input' / filename
    with open(data_file) as file:
        return [int(d.strip()) for d in file.readlines()]


data = read_data('day1.txt')
solution1 = [calc_fuel(n) for n in data]

print(f'Solation day1 - part 1: {sum(solution1)}')

solution2 = calc_fuel_p2(1969)
print([a for a in solution2])
print(f'Solation day1 - part 2: {sum(solution2)}')

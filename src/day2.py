from pathlib import Path
from typing import List


class Computer:
    program: List[int]

    def __init__(self, program: List[int]):
        self.pointer = 0
        self.program = program

    def execute(self):
        op_code = self.program[self.pointer]
        operand1_addr = self.program[self.pointer + 1]
        operand2_addr = self.program[self.pointer + 2]
        output_addr = self.program[self.pointer + 3]
        if op_code == 1:
            result = self.program[operand1_addr] + self.program[operand2_addr]
        if op_code == 2:
            result = self.program[operand1_addr] * self.program[operand2_addr]
        self.program[output_addr] = result
        self.pointer += 4
        return self.halt_program()

    def halt_program(self) -> bool:
        return self.program[self.pointer] != 99

    def setup(self):
        self.program[1] = 12
        self.program[2] = 2


def read_input(file_name: str) -> List[int]:
    data_file = Path(__file__).parent.parent.absolute() / 'input' / file_name
    with open(data_file, 'r') as file:
        return [int(i.strip()) for i in file.read().split(',')]


RAW = """1,9,10,3,2,3,11,0,99,30,40,50"""

program = read_input('day2.txt')
# program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

prog = Computer(program)
prog.setup()
while True:
    if not prog.execute():
        break

print(f'Solution Day2 - part1: {prog.program[0]}')

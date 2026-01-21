from aocd import get_data
import re

puzzle_input = get_data(day=3, year=2024)

QUESTION_PART = 2

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

#X and Y are 1-3 digit numbers
#mul(x,y) = X * Y
#ignore every other character

def input_into_list_of_instructions(puzzleinput: str) -> list[tuple[str]]:
    if QUESTION_PART == 2:
        instructions_list = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", puzzleinput)
    else:
        instructions_list = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', puzzleinput)
    instructions_list = [(tuple(x for x in _ if x)) for _ in instructions_list]
    return instructions_list

def process_instructions(instr_list: list[tuple[str]]) -> int:
    result = 0
    enabled=True
    for instr in instr_list:
        if instr[0] == "do()":
            enabled=True
        elif instr[0] == "don't()":
            enabled=False
        elif enabled:
            nums = instr[0][4:-1]
            num1, num2 = nums.split(",")
            result += int(num1) * int(num2)
    return result

inst = input_into_list_of_instructions(puzzle_input)
results = process_instructions(inst)
print("Answer: ", results)


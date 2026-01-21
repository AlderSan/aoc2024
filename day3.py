from aocd import get_data
import re

puzzle_input = get_data(day=3, year=2024)

QUESTION_PART = 1

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

#X and Y are 1-3 digit numbers
#mul(x,y) = X * Y
#ignore every other character

def input_into_list_of_instructions(puzzleinput: str) -> list[str]:
    instructions_list = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', puzzleinput)
    return instructions_list

def process_instructions(instr_list: list[str]) -> int:
    result = 0
    for instr in instr_list:
        nums = instr[4:-1]
        print(nums)
        num1, num2 = nums.split(",")
        result += int(num1) * int(num2)
    return result

inst = input_into_list_of_instructions(puzzle_input)
results = process_instructions(inst)
print("Answer: ", results)


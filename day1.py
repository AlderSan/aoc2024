from aocd import get_data

puzzle_input = get_data(day=1, year=2024)

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

QUESTION_PART = 2

def input_into_sorted_lists(input: str) -> tuple[list[int],list[int]]:
    columns = input.split("\n")
    left_list = []
    right_list = []
    for item in columns:
        left, right = item.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    return sorted(left_list), sorted(right_list)

def multiply_and_sum_distance_between(list1: list[int], list2: list[int]) -> int:
    total = 0
    for i in range(0, len(list1)):
        dif = abs(list1[i] - list2[i])
        total += dif
    return total

def sum_similarity_scores(list1: list[int], list2: list[int]) -> int:
    total = 0
    for number in list1:
        count = list2.count(number)
        total += number * count
    return total

if QUESTION_PART == 1:
    left_list, right_list = input_into_sorted_lists(puzzle_input)
    total_difference = multiply_and_sum_distance_between(left_list, right_list)
    print("Answer: ", total_difference)
if QUESTION_PART == 2:
    left_list, right_list = input_into_sorted_lists(puzzle_input)
    total_similarity_scores = sum_similarity_scores(left_list,right_list)
    print("Answer: ", total_similarity_scores)

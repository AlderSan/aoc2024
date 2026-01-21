from aocd import get_data

puzzle_input = get_data(day=5, year=2024)

QUESTION_PART = 1

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def input_into_rules_updates(puzzleinput: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules, updates = puzzleinput.split("\n\n", 2)
    rules_lines = rules.split("\n")
    rules_list = []
    for rule in rules_lines:
        rules_list.append(tuple(rule.split("|")))
    updates_lines = updates.split("\n")
    updates_list = []
    for update in updates_lines:
        updates_list.append(update.split(","))
    return rules_list, updates_list

def check_rules(rules_list: list[tuple[int, int]], update: list[int]) -> bool:
    rule_check_results = []
    for rule in rules_list:
        first_num, second_num = rule
        if first_num in update and second_num in update:
            rule_check_results.append(update.index(first_num) < update.index(second_num))
    return all(rule_check_results)

def check_all_updates(rules_list: list[tuple[int, int]], update_list: list[list[int]]) -> list[list[int]]:
    valid_updates = []
    for update in update_list:
        if check_rules(rules_list, update):
            valid_updates.append(update)
    return valid_updates

def sum_middle_value(valid_updates_list: list[list[int]]) -> int:
    result = 0
    for valid_update in valid_updates_list:
        result += int(valid_update[len(valid_update) // 2])
    return result

rules, updates = input_into_rules_updates(puzzle_input)
valid_updates = check_all_updates(rules, updates)
count = sum_middle_value(valid_updates)
print("Answer: ", count)
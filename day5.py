from aocd import get_data
from typing import Any

puzzle_input = get_data(day=5, year=2024)

QUESTION_PART = 2

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

def fix_invalid_updates(rules_list: list[tuple[int, int]], invalid_update_list: list[list[int]]) -> list[list[int]]:
    fixed_updates = []
    for update in invalid_update_list:
        fixed_update = update
        while not check_rules(rules_list, fixed_update):
            failed_rules = check_rules(rules_list, update, return_failed=True)
            for rule in failed_rules:
                while not check_rules([rule], fixed_update):
                    fixed_update.insert(fixed_update.index(rule[0]) - 1, fixed_update.pop(fixed_update.index(rule[0])))
        fixed_updates.append(fixed_update)
    return fixed_updates

def check_rules(rules_list: list[tuple[int, int]], update: list[int], return_failed=False) -> Any:
    rule_check_results = []
    failed_list = []
    for rule in rules_list:
        first_num, second_num = rule
        if first_num in update and second_num in update:
            result = update.index(first_num) < update.index(second_num)
            rule_check_results.append(result)
            if not result:
                failed_list.append(rule)
    if return_failed:
        return failed_list
    else:
        return all(rule_check_results)

def check_all_updates(rules_list: list[tuple[int, int]], update_list: list[list[int]]) -> list[list[int]]:
    valid_updates = []
    invalid_updates = []
    for update in update_list:
        if check_rules(rules_list, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    if QUESTION_PART == 1:
        results = valid_updates
    else:
        results = fix_invalid_updates(rules_list, invalid_updates)
    return results

def sum_middle_value(valid_updates_list: list[list[int]]) -> int:
    result = 0
    for valid_update in valid_updates_list:
        result += int(valid_update[len(valid_update) // 2])
    return result

rules, updates = input_into_rules_updates(puzzle_input)
results = check_all_updates(rules, updates)
count = sum_middle_value(results)
print("Answer: ", count)
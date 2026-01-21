from aocd import get_data
from numpy import diff

puzzle_input = get_data(day=2, year=2024)

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

#row is report
#valid if: levels are either all increasing or all decreasing AND
#difference between levels is 1 <= diff <= 3

def input_into_reports(input: str) -> list[list[int]]:
    split_lines = input.split("\n")
    reports = []
    for line in split_lines:
        reports.append(list(map(int, line.split())))
    return reports


def is_valid_report(report: list[int]) -> bool:
    if report == sorted(report) or report == sorted(report, reverse=True):
        rdiff = diff(report)
        return all([abs(n) >= 1 and abs(n) <= 3 for n in rdiff])
    else:
        return False

def check_all_reports(list_of_reports: list[list[int]]) -> list[tuple[int, bool]]:
    results = []
    for report in list_of_reports:
        results.append((list_of_reports.index(report), is_valid_report(report)))
    return results

def count_valids(list_of_results: list[tuple[int, bool]]) -> int:
    count = 0
    for results in list_of_results:
        if results[1]:
            count += 1
    return count

reports = input_into_reports(puzzle_input)
valid_reports = check_all_reports(reports)
valid_count = count_valids(valid_reports)
print(len(puzzle_input.split("\n")))
print("Valid reports:", *valid_reports, sep="\n")
print("Count: ", valid_count)
print(puzzle_input.split("\n")[594])
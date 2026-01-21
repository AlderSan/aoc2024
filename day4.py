from aocd import get_data
import re

puzzle_input = get_data(day=4, year=2024)

QUESTION_PART = 2

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def input_into_matrix(puzzleinput: str) -> list[list[str]]:
    rows = puzzleinput.split("\n")
    matrix = []
    for row in rows:
        column = list(row)
        matrix.append(column)
    return matrix

def check_for_xmas(row: int, column: int, matrix: list[list[str]]) -> int:
    xmas = 0
    #working from a located X, checking directions
    if row >= 3:
        #up
        if (matrix[row - 1][column] == "M" and
            matrix[row - 2][column] == "A" and
            matrix[row - 3][column] == "S"):
            xmas += 1
    if row <= len(matrix) - 4:    
        #down
        if (matrix[row + 1][column] == "M" and
            matrix[row + 2][column] == "A" and
            matrix[row + 3][column] == "S"):
            xmas += 1
    if column >= 3:
        #left
        if (matrix[row][column - 1] == "M" and
            matrix[row][column - 2] == "A" and
            matrix[row][column - 3] == "S"):
            xmas += 1
    if column <= len(matrix[0]) - 4:
        #right
        if (matrix[row][column + 1] == "M" and
            matrix[row][column + 2] == "A" and
            matrix[row][column + 3] == "S"):
            xmas += 1
    if row >= 3 and column >= 3:
        #UL
        if (matrix[row - 1][column - 1] == "M" and
            matrix[row - 2][column - 2] == "A" and
            matrix[row - 3][column - 3] == "S"):
            xmas += 1
    if row >= 3 and column <= len(matrix[0]) - 4:
        #UR
        if (matrix[row - 1][column + 1] == "M" and
            matrix[row - 2][column + 2] == "A" and
            matrix[row - 3][column + 3] == "S"):
            xmas += 1
    if row <= len(matrix) - 4 and column >= 3:
        #DL
        if (matrix[row + 1][column - 1] == "M" and
            matrix[row + 2][column - 2] == "A" and
            matrix[row + 3][column - 3] == "S"):
            xmas += 1
    if row <= len(matrix) - 4 and column <= len(matrix[0]) - 4:
        #DR
        if (matrix[row + 1][column + 1] == "M" and
            matrix[row + 2][column + 2] == "A" and
            matrix[row + 3][column + 3] == "S"):
            xmas += 1
    return xmas

def find_xmas(matrix: list[list[str]]) -> int:
    count = 0
    found = []
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            if matrix[row][column] == "X" and QUESTION_PART == 1:
                count += check_for_xmas(row, column, matrix)
            elif matrix[row][column] == "A" and QUESTION_PART == 2:
                count += check_for_x_mas(row, column, matrix)
    return count


def check_for_x_mas(row: int, column: int, matrix: list[list[str]]) -> int:
    x_mas=0
    #working from a located middle A
    if row >= 1 and row <= len(matrix) - 2 and column >= 1 and column <= len(matrix[0]) - 2:
        word1 = matrix[row-1][column-1] + matrix[row][column] + matrix[row+1][column+1]
        word2 = matrix[row+1][column-1] + matrix[row][column] + matrix[row-1][column+1]
        if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
            x_mas += 1
    return x_mas



matrix = input_into_matrix(puzzle_input)
count = find_xmas(matrix)
print("Answer: ", count)
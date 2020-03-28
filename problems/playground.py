# def wordsOne(matrix, string):
#     pointer = 0
#     for row_i in range(len(matrix)):
#         for col_i in range(len(matrix[0])):
#             cell = matrix[row_i][col_i]
#             matrix[row_i][col_i] = string[pointer %
#                                           len(string)] if cell else "."
#             pointer += 1 if cell else 0
#         print(matrix[row_i])
#     return matrix


# testMatrix = [
#     [1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1]
# ]
# wordsOne(testMatrix, "JPMC")

import math
[0, 0, 0, 0, 0, 0, 0, 0, 0]


def wordsTwo(matrix, string):
    dim = math.sqrt(len(matrix))
    grid, row = [], []
    j = 0
    for i in range(len(matrix)):
        if len(row) == dim:
            grid.append(row)
            print(row)
            row = []
        row.append(string[j % len(string)] if matrix[i] == "1" else ".")
        j += 1 if matrix[i] == "1" else 0
    print(row)
    grid.append(row)
    return grid


testMatrix = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
wordsTwo("0000011110111111100000000", "CodeCommit!")

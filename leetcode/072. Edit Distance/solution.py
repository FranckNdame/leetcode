# Solution 1: Top-down approach
def levenshteinDistance(str1, str2):
    return levRec(str1, str2)

def levRec(str1, str2, cache={}):
    # Base case
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    if hash(str1, str2) not in cache:
        if str1[-1] == str2[-1]:
            cache[hash(str1, str2)] = levRec(str1[:-1], str2[:-1], cache)
        else:
            replace = levRec(str1[:-1], str2[:-1], cache) + 1
            insert = levRec(str1, str2[:-1], cache) + 1
            delete = levRec(str1[:-1], str2, cache) + 1
            cache[hash(str1, str2)] = min(replace, insert, delete)

    return cache[hash(str1, str2)]


def hash(str1, str2):
    return f"{str1}->{str2}"

# Solution 2: Bottom-up approach
def editDistance(str1, str2):
    matrix = initilaizeMatrix(str1, str2)
    for row_i in range(1, len(matrix)):
        for col_i in range(1, len(matrix[0])):
            if str2[row_i - 1] == str1[col_i - 1]:
                matrix[row_i][col_i] = matrix[row_i - 1][col_i - 1]
            else:
                insert = matrix[row_i - 1][col_i] + 1
                replace = matrix[row_i - 1][col_i - 1] + 1
                delete = matrix[row_i][col_i - 1] + 1
                matrix[row_i][col_i] = min(insert, replace, delete)
    return matrix[-1][-1]


def initilaizeMatrix(str1, str2):
    matrix = [[0 for i in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    matrix[0] = [i for i in range(len(str1)+1)]
    for i in range(1, len(str2) + 1):
        matrix[i][0] = i
    return matrix
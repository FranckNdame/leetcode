def numbersInPi(pi, numbers):
    lookup = {number: True for number in numbers}
    minSpace = getMinSpace(pi, lookup, {}, 0)
    return -1 if minSpace == float("inf") else minSpace


def getMinSpace(pi, lookup, cache, startIdx):
        # Base case
    if startIdx == len(pi):
        return -1
    if startIdx in cache:
        return cache[startIdx]

    minSpace = float('inf')
    for i in range(startIdx, len(pi)):
        subStr = pi[startIdx: i+1]
        if subStr in lookup:
            currMinSpace = 1 + getMinSpace(pi, lookup, cache, i+1)
            minSpace = min(minSpace, currMinSpace)

    cache[startIdx] = minSpace
    return cache[startIdx]

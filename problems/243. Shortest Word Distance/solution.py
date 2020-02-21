class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        lookup = collections.defaultdict(list)
        for index, word in enumerate(words):
            lookup[word].append(index)
        pA = pB = 0
        shortestDistance = float('inf')
        listA, listB = lookup[word1], lookup[word2]

        while pA < len(listA) and pB < len(listB):
            shortestDistance = min(
                shortestDistance, abs(listA[pA] - listB[pB]))
            if listA[pA] < listB[pB]:
                pA += 1
            else:
                pB += 1

        return 0 if shortestDistance == float('inf') else shortestDistance

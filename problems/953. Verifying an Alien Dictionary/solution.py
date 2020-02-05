class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {word: index for index, word in enumerate(order)}
        for i in range(len(words)-1):
            if not self.isSorted(words[i], words[i+1], lookup):
                return False
        return True

    def isSorted(self, wordOne, wordTwo, lookup):
        i = 0
        while i < min(len(wordOne), len(wordTwo)) and wordOne[i] == wordTwo[i]:
            i += 1

        if i == len(wordTwo):
            return False

        while i < min(len(wordOne), len(wordTwo)):
            if lookup[wordOne[i]] > lookup[wordTwo[i]]:
                return False
            elif lookup[wordOne[i]] < lookup[wordTwo[i]]:
                return True
            else:
                i += 1

        return True

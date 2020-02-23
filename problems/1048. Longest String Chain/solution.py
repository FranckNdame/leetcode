class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = list(map(lambda x: "".join(sorted(x)), words))
        adj_list = self.constructAdjList(words)
        visits = {}
        self.longest = 1

        def dfs(word, adj_list, visits):
            stack = [(word, 1)]

            while stack:
                currWord, length = stack.pop()
                self.longest = max(self.longest, length)
                for nWord in adj_list[currWord]:
                    visits[nWord] = True
                    stack.append((nWord, length+1))

        for word in words:
            if word not in visits:
                visits[word] = True
                dfs(word, adj_list, visits)

        return self.longest

    def constructAdjList(self, words):
        adj_list = {word: [] for word in words}
        for i in range(len(words)-1, -1, -1):
            word = words[i]
            for j in range(len(word)):
                newWord = word[:j] + word[j+1:]
                if newWord in adj_list:
                    adj_list[newWord].append(word)
        return adj_list

class Solution:
    def findJudge(self, N, trust):
        degrees = [0]*N
        for t in trust:
            out, in_ = t[0], t[1]
            degrees[out-1] -= 1
            degrees[in_-1] += 1
        print(degrees)
        for index, degree in enumerate(degrees):
            if degree == N-1:
                return index+1

        return -1

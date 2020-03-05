class Solution:

    def countPrimes(self, n: int):
        table = [0]*n
        count = 0

        for num in range(2, n):
            if table[num] == 1:
                continue
            count += 1
            temp = num*num
            while temp < n:
                table[temp] = 1
                temp += num
        return count

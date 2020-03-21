class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        return self.helper(num, lookup)

    def helper(self, num, lookup):
        if not num:
            return ''
        if num in lookup:
            return lookup[num]

        zeros = len(str(num)) - 1
        unit = 10**zeros

        if (num//unit) == 9:
            return lookup[9*unit] + self.helper(num % (9*unit), lookup)
        elif num > (5*unit):
            return lookup[5*unit] + self.helper(num % (5*unit), lookup)
        else:
            return lookup[unit] + self.helper(num-unit, lookup)


sol = Solution()
for num in [1, 2, 3, 5, 7, 9, 15, 19, 50, 49, 150, 333]:
    print(sol.intToRoman(num))

# "MCMXCIV"

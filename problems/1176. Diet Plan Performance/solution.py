class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        currKal = sum(calories[:k])
        if currKal < lower:
            points -= 1
        if currKal > upper:
            points += 1

        for i in range(k, len(calories)):
            l, r = calories[i - k], calories[i]
            currKal = currKal - l + r
            if currKal < lower:
                points -= 1
            if currKal > upper:
                points += 1

        return points

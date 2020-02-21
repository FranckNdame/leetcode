class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints:
            return
        timePoints = list(map(self.toInt, timePoints))
        timePoints.sort()
        minDiff = float('inf')

        for i in range(len(timePoints)-1):
            minDiff = min(minDiff, timePoints[i+1] - timePoints[i])
            if minDiff == 0:
                return minDiff

        minDiff = min(minDiff, (24*60 - (timePoints[-1] - timePoints[0])))
        return minDiff

    def toInt(self, x):
        hr, m = x.split(":")
        return (int(hr) * 60) + int(m)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        lMax = 0
        rMaxes = [0]*len(height)
        rMaxes[-1] = height[-1]
        for i in range(len(height) - 2, 0, -1):
            rMaxes[i] = max(rMaxes[i+1], height[i+1])

        for i in range(1, len(height)-1):
            lMax = max(height[i-1], lMax)
            rMax = rMaxes[i]
            waterHeight = min(lMax, rMax) - height[i]
            result += waterHeight if waterHeight > 0 else 0

        return result

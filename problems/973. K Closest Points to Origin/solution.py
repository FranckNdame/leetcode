class Solution:
    # Approach 1
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = sorted(points, key=lambda point: self.toDistance(point))
        return result[:K]

    def toDistance(self, point):
        return (point[0]*point[0])+(point[1]*point[1])

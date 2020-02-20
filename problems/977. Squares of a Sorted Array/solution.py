class Solution:
    # Approach 1
    def sortedSquares(self, A: List[int]) -> List[int]:
        # O(n) time complexity
        A = list(map(lambda x: x**2, A))
        # O(nlogn) time complexity
        return sorted(A)

    # Approach 2
    def sortedSquares(self, A: List[int]) -> List[int]:
        lhs, rhs = 0, len(A) - 1
        result = [0] * len(A)
        slot = len(A) - 1

        while lhs <= rhs:
            l, r = A[lhs]**2, A[rhs]**2
            if l >= r:
                result[slot] = l
                lhs += 1
            else:
                result[slot] = r
                rhs -= 1
            slot -= 1
        return result

    # Approach 3
    def sortedSquares(self, A: List[int]) -> List[int]:
        list1, list2 = [], []
        p = len(A)-1

        while p >= 0:
            if A[p] < 0:
                break
            p -= 1
        list1 = list(map(lambda x: abs(x), A[:p+1]))[::-1]
        list2 = A[p+1:]
        p1, p2 = 0, 0
        result = []

        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] < list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1

        if p1 < len(list1):
            result.extend(list1[p1:])
        if p2 < len(list2):
            result.extend(list2[p2:])

        return list(map(lambda x: x**2, result))

class Solution:
    
    def findUnsortedSubarray(self, array):
        if len(array) <= 1: return 0
        result = [float('inf'), -float('inf')]

        for i in range(len(array)):
            if self.isOutOfOrder(i, array):
                self.goLeft(i, array, result)
                self.goRight(i, array, result)

        return (result[1] - result[0]) + 1 if result[0] != float('inf') else 0

    def isOutOfOrder(self, i, array):
        if i == 0:
            return array[i] > array[i+1]
        if i == len(array) - 1:
            return array[i] < array[i-1]

        return (array[i] > array[i+1]) or (array[i] < array[i-1])


    def goLeft(self, i, array, result):
        j = i
        while j > 0 and array[i] < array[j-1]:
            j -= 1
        result[0] = min(result[0], j)

    def goRight(self, i, array, result):
        j = i
        while j < len(array)-1 and array[i] > array[j+1]:
            j += 1
        result[1] = max(result[1], j)




        
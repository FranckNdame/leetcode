# Time Complexity: O(n) || Space Complexity: O(n)
def maxSubsetSumNoAdjacent(array):
	if not array: return 0
	if len(array) < 2: return array[0]
	
	maxSums = [None for _ in range(len(array))]
	maxSums[0], maxSums[1] = array[0], max(array[0], array[1])
	
	for i in range(2, len(array)):
		maxSums[i] = max(maxSums[i-1], array[i] + maxSums[i-2])
		
	return maxSums[-1]

# Time Complexity: O(n) || Space Complexity: O(1)
def maxSubsetSumNoAdjacent(array):
	if not array: return 0
	if len(array) < 2: return array[0]
	
	secondPrev = array[0]
	prev = max(array[0], array[1])
	result = prev
	
	for i in range(2, len(array)):
		result = max(array[i] + secondPrev, prev)
		temp = prev
		prev = result
		secondPrev = temp
		
	return result

		

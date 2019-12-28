# Solution 1: Using a Hashtable
# Time Complexity: O(n) || Space Complexity: (n) 
def threeNumberSum(array, targetSum):
 	lookup = { i for i in array }
 	array.sort()
 	triplets = []
 	for i in range(len(array)):
 		for j in range(i+1,len(array)):
 			k = targetSum - array[i] - array[j]
 			if k in lookup and array[j] < k:
 				triplets.append([array[i], array[j], k])
 	return triplets


# Solution 2: Using pointers
# Time Complexity: O(n) || Space Complexity: (n) 
def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		lhs = i + 1
		rhs = len(array) - 1
		while lhs < rhs:
			currentSum = array[i] + array[lhs] + array[rhs]
			if currentSum == targetSum:
				triplets.append([array[i], array[lhs], array[rhs]])
				lhs += 1
				rhs -= 1
			elif currentSum < targetSum:
				lhs += 1
			else:
				rhs -= 1
	return triplets

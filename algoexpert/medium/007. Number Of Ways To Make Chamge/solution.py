# Time Complexity: O(nd) || Space Complexity: O(n)
def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for i in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for i in range(1, n+1):
			if i < denom: continue
			ways[i] = ways[i] + ways[i-denom]
	return ways[n]
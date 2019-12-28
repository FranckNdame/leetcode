# Time Complexity: O(nd) || Space Complexity: O(n)
def minNumberOfCoinsForChange(n, denoms):
	minCoins = [float('inf')  for _ in range(n+1)]
	minCoins[0] = 0
	for denom in denoms:
		for i in range(1,n+1):
			if denom > i: continue
			minCoins[i] = min(minCoins[i], 1 + minCoins[i - denom])
	return minCoins[n] if minCoins[n] != float('inf') else -1
	

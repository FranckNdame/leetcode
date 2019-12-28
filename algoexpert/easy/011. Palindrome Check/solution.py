# Time Complexity: O(n) || Space Complexity: O(1)
def isPalindrome(string):
	lhs, rhs = 0, len(string) - 1
	
	while lhs < rhs:
		if string[lhs] != string[rhs]:
			return False
		lhs += 1
		rhs -= 1
	return True
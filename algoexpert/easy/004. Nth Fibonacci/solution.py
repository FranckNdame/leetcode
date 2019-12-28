# Solution 1: Recursive
# Time Complexity: O(n) || Space Complexity: O(n)
def fibonacci(n, lookup={1:0, 2:1}):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n <= 0:
        raise ValueError("n must be a postive integer")

    if n in lookup: return lookup[n]
    lookup[n] = fibonacci(n-1, lookup) + fibonacci(n-2, lookup)

    return lookup[n]


# Solution 2: Iterative
# Time Complexity: O(n) || Space Complexity: O(1)
def fibonacci2(n):
    prev1, prev2 = 1, 1
    for _ in range(2, n):
        x = prev1 + prev2
        temp = prev1
        prev1 = x
        prev2 = temp
    return x

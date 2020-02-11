def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) + (n & 1)
        n >>= 1
    return res


print(0 & 1)

"""

    0101 AND 0001

    0001

"""

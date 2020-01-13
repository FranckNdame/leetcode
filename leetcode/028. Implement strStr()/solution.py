def strStr(self, haystack: str, needle: str) -> int:
    if not needle:return 0
    if haystack == needle: return 0

    lenH = len(haystack)
    lenN = len(needle)
    if lenN >= lenH:
        return -1

    for i in range(lenH - lenN + 1):
        if haystack[i:i+lenN] == needle:
            return i

    return -1

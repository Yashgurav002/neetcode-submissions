class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)

        for i in range(n-m+1): #bcs this will be the last position to find the string
            if haystack[i:i+m]==needle:
                return i

        return -1
        
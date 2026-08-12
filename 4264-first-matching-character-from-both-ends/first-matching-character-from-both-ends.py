class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        
        for i in range(n):
            if s[i]==s[n-i-1]:
                return i
            pass
        return -1

        return (array[0])

        
class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        
        for i in range(1, len(s)):
            if s[i - 1] != s[i] and count[s[i - 1] ] == int(s[i - 1]) and count[s[i]] == int(s[i]):
                return s[i-1] + s[i]
            
        return ''
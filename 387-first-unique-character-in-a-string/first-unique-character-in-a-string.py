class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounter = Counter(s)
        for i in range(len(s)):
            if sCounter[s[i]] == 1:
                return i
        return -1
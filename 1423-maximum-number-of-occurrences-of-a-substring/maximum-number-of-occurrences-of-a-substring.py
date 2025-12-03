class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        
        for index in range(len(s) - minSize + 1):
            substring = s[index: index + minSize]
            if len(set(substring)) <= maxLetters:
                freq[substring] = freq.get(substring, 0) + 1
        
        if freq:
            return max(freq.values())
        return 0
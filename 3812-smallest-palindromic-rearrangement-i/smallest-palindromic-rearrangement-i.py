class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)
        
        sorted_s = sorted(s[: length // 2])
        letter = ''
        if length % 2:
            letter = s[length // 2]

        return ''.join(sorted_s) + letter + ''.join(sorted_s[::-1])
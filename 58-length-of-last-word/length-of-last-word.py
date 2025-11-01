class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = [word for word in s.strip().split()]
        return len(s_list[-1])
    
class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = []
        i = 0
        for i in range(len(s)):
            if s[i].isdigit():
                s_list.pop()
            else:
                s_list.append(s[i])
        return ''.join(s_list)
    

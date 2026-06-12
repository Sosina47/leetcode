class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)): 
            if goal[0] == s[i]: 
                if s[i: ] + s[:i] == goal: 
                    return True

        return False

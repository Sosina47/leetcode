class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        count_open = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                count_open += 1
            else:
                count_open -= 1
                if s[i - 1] == '(':
                    score += 2 ** count_open
                stack.pop()
            
        return score
                

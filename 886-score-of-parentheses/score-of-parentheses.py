class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        count_open = 0
        for i in range(len(s)):
            if s[i] == '(':
                count_open += 1
            else:
                count_open -= 1
                if s[i - 1] == s[i]:
                    continue
                    
                score += 1 if count_open == 0 else 2 ** count_open

        return score 
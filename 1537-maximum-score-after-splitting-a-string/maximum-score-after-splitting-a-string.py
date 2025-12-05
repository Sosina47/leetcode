class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        ps = []
        for index in range(len(s)):
            if index == 0:
                ps.append(int(s[index]))
            else:
                ps.append(int(s[index]) + ps[index - 1])
        
        for i in range(len(ps)-1):
            curr_score = (i + 1) - ps[i] + ps[-1] - ps[i]
            max_score = max(max_score, curr_score)

        return max_score
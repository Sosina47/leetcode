class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        total = sum(cardPoints)
        left = 0
        curr_sum = 0
        max_score = 0
        for right in range(len(cardPoints)):
            curr_sum += cardPoints[right]
            if right - left + 1 > len(cardPoints) - k:
                curr_sum -= cardPoints[left] 
                left += 1

            if right - left + 1 == len(cardPoints) - k:
                max_score = max(max_score, total - curr_sum)

        return max_score 
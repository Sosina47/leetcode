class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = max_length = most_frequent = 0
        freq = {}
        
        for right in range(len(answerKey)):
            freq[answerKey[right]] = freq.get(answerKey[right], 0) + 1
            most_frequent = max(most_frequent, freq[answerKey[right]])

            while right - left + 1 - most_frequent > k:
                if freq[answerKey[left]] == 1:
                    freq.pop(answerKey[left])
                else:
                    freq[answerKey[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
    
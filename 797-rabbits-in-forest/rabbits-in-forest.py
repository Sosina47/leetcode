class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0
        
        
        for key, val in freq.items():
            if key == 0:
                total += val

            else:
                min_ = ceil(val / (key + 1))
                total += min_ * (key + 1)
                
        return total